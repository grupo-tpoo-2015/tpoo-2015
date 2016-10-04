/*migrar participantes*/
insert into usability_tests_executions_participant(id, name)
select user_id, user_name
from tpoodump.users;

/*migra refactorings*/
insert into usability_tests_refactoring(id, name)
select id, name
from tpoodump.refactorings;

/*migra usability tests*/
SET @idSuperUser =
(select min(id)
 from auth_user
 where is_superuser);

insert into usability_tests_usabilitytest(id, name, owner_id)
select id, `name`, @idSuperUser
from tpoodump.usability_test;

/*crea las versiones*/
insert into usability_tests_appversion(id, name, usability_test_id)
select id, "Non Refactored", usability_test_id
from tpoodump.scenario
where name like "%Non Refactored";

insert into usability_tests_appversion(id, name, usability_test_id)
select id, "Refactored", usability_test_id
from tpoodump.scenario
where name not like "%Non Refactored";

/*migra tasks*/
insert into usability_tests_task(id, name, usability_test_id)
select project_id, project_name, usability_test_id
from tpoodump.task;


/*migra scenarios*/
insert into usability_tests_scenario(id, name, app_version_id)
select S.id, S.name, AV.id
from tpoodump.scenario S inner join usability_tests_appversion AV on (S.usability_test_id = AV.usability_test_id)
where (S.name like '%Non Refactored' and AV.name ='Non Refactored') or
	  (S.name not like '%Non Refactored' and AV.name ='Refactored');

/*migra scenario_task, lo que antes era task_for_version*/
insert into tasks_scenariotask(id, scenario_id, task_id)
select id, scenario_id, task_id
from tpoodump.task_version;

/*migra interaction step para cada task*/
insert into tasks_interactionstep(id, scenario_task_id, is_question, name, `order`)
select id, task_version_id, question, name, step_order
from tpoodump.step S;

/*relacion entre scenario_task y refactoring -many to many, TODO en el modelo
la relacion entre refactoring y appVersion vuela.
Se reemplaza por metodo que hace las queries necesarias
*/
insert into tasks_scenariotask_refactorings(scenariotask_id, refactoring_id)
select task_version_id, refactoring_id
from(
  select task_version_id, refactoring_id
  from tpoodump.step
  where (refactoring_id is not null) and (refactoring_id <> 0)

  UNION ALL

  select task_version_id, second_refactoring_id
  from tpoodump.step
  where (second_refactoring_id is not null) and (second_refactoring_id <> 0)

  UNION ALL

  select task_version_id, third_refactoring_id
  from tpoodump.step
  where (third_refactoring_id is not null) and (third_refactoring_id <> 0)
) T

  group by task_version_id, refactoring_id;

/*migra scenario execution*/
insert into usability_tests_executions_scenarioexecution(id, participant_id, scenario_id)
select id, user_id, scenario_id
from tpoodump.scenario_execution;

/*migra task execution*/
insert into usability_tests_executions_taskscenarioexecution(id, scenario_execution_id, scenario_task_id)
select id, scenario_execution_id, task_version_id
from tpoodump.task_execution;

/*migra los interaction_step_execution*/
insert into usability_tests_executions_interactionstepexecution(id, interaction_step_id, task_scenario_execution_id)
select SE.id, SE.step_id, SE.task_execution_id
from tpoodump.step_execution SE inner join tpoodump.step S on (SE.step_id = S.id);

/*plantea la observación tiempo*/
insert into tasks_observationtype(id, name, unit)
values (1,'Tiempo', 'seconds');

/*plantea la observación demográficas*/
insert into tasks_observationtype(id, name, unit)
values (2,'Preguntas demográficas', 'free');

/*plantea la observación satisfacción*/
insert into tasks_observationtype(id, name, unit)
values (3,'Preguntas de satisfacción', '1..5');

/*guarda el observation tiempo para step que no son preguntas*/
insert into tasks_interactionstep_observation_types(interactionstep_id, observationtype_id)
select id, 1 /*el tiempo sólo a los que no son question*/
from tpoodump.step
where not question;

/*guarda el observation dem para step que son preguntas demográficas*/
insert into tasks_interactionstep_observation_types(interactionstep_id, observationtype_id)
select id, 2
from tpoodump.step
where question
  and ((name like 'Ingrese su edad:')
  or  (name like 'Ha trabajado o trabaja en:')
  or  (name like 'FormaciÃ³n acadÃ©mica:'));

/*guarda el observation satisfaction para step que no son preguntas demográficas ni time*/
insert into tasks_interactionstep_observation_types(interactionstep_id, observationtype_id)
select distinct(S.id), 3
from tpoodump.step S inner join tpoodump.step_execution SE on (S.id = SE.step_id)
where question
  and not((name like 'Ingrese su edad:')
  or  (name like 'Ha trabajado o trabaja en:')
  or  (name like 'FormaciÃ³n acadÃ©mica:'))
and (length(SE.result)= 1);

insert into usability_tests_executions_observation(`value`, observation_type_id, step_execution_id)
/*esta consulta agrega el observation_type time */
select SE.time, 1, SE.id
from tpoodump.step S inner join tpoodump.step_execution SE on (S.id = SE.step_id)
where not question;

insert into usability_tests_executions_observation(`value`, observation_type_id, step_execution_id)
/*esta consulta agrega el observation_type satisfaction */
select cast(SE.result AS DECIMAL(10,2)), 3, SE.id
from tpoodump.step S inner join tpoodump.step_execution SE on (S.id = SE.step_id)
where question
  and not((name like 'Ingrese su edad:')
  or  (name like 'Ha trabajado o trabaja en:')
  or  (name like 'FormaciÃ³n acadÃ©mica:'))
and (length(SE.result)= 1);


