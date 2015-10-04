/*migrar participantes*/
insert into usability_tests_executions_participant(id, name)
select user_id, user_name
from tpoodump.users;

/*migra usability tests*/
SET @idSuperUser = 
(select min(id)
 from auth_user
 where is_superuser);

insert into usability_tests_usabilitytest(id, name, owner_id)
select *, @idSuperUser
from tpoodump.usability_test;

/*migra tasks*/
insert into usability_tests_task(id, name, usability_test_id)
select project_id, project_name, usability_test_id
from tpoodump.task;

/*crea las versiones*/
insert into usability_tests_appversion(name, usability_test_id)
select "Non Refactored", usability_test_id
from tpoodump.scenario
where name like "%Non Refactored";

insert into usability_tests_appversion(name, usability_test_id)
select "Refactored", usability_test_id
from tpoodump.scenario
where name not like "%Non Refactored";

/*migra scenarios*/
insert into usability_tests_scenario(id, name, app_version_id)
select S.id, S.name, AV.id
from tpoodump.scenario S inner join usability_tests_appversion AV on (S.usability_test_id = AV.usability_test_id)
where (S.name like '%Non Refactored' and AV.name ='Non Refactored') or 
	  (S.name not like '%Non Refactored' and AV.name ='Refactored');

/*migra refactorings*/
insert into usability_tests_refactoring(id, name)
select id, name
from tpoodump.refactorings;

/*migra scenario_task, lo que antes era task_for_version*/
insert into tasks_scenariotask(id,scenario_id, task_id)
select id, scenario_id, task_id
from tpoodump.task_version;

/*relacion entre scenario_task y refactoring -many to many, TODO en el modelo 
la relacion entre refactoring y appVersion vuela. Se reemplaza por metodo que hace las queries necesarias
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
where (third_refactoring_id is not null) and (third_refactoring_id <> 0)) T
group by task_version_id, refactoring_id;

/*migra step*/
insert into tasks_interactionstep(id, scenario_task_id, is_question, name, `order`)
select id, task_version_id, question, name, step_order
from tpoodump.step;

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
select id, step_id, task_execution_id
from tpoodump.step_execution;

/*plantea 3 tipos de observaciones posibles, para los datos de la base de datos que hay cargados*/
insert into tasks_observationtype(id, name, unit)
values (1,'done', 'boolean');

insert into tasks_observationtype(id, name, unit)
values (2,'time', 'seconds');

/*insert into tasks_observationtype(id, name, unit)
values (3,'question', 'boolean');*/

/*a todos los interaction steps se le pueden observar si están realizados o no. 
si son de tipo question se puede observar si contestó o no
a los que no son tipo question y estan terminadas se les pueden observar el tiempo*/

insert into tasks_interactionstep_observation_types(interactionstep_id, observationtype_id)
select id, 1 /*a todos los pasos si está realizado o no*/ 
from tpoodump.step;

insert into tasks_interactionstep_observation_types(interactionstep_id, observationtype_id)
select id, 2 /*el tiempo sólo a los que no son question*/ 
from tpoodump.step
where not question;

insert into usability_tests_executions_observation(`value`, observation_type_id, step_execution_id)
/*esta consulta resuelve si un paso de ejecución está resuelto o no*/
select done, 1, T.id as step_execution_id
from (
select SE.id , 
       (case when (result = '0') then false
             when (result like '-%') then false
            else true end) as done
from tpoodump.step S inner join tpoodump.step_execution SE on (S.id = SE.step_id)
where question

UNION ALL

select SE.id, (case when result like '%skip%' then false else true end) as done
from tpoodump.step S inner join tpoodump.step_execution SE on (S.id = SE.step_id)
where not question ) T;

insert into usability_tests_executions_observation(`value`, observation_type_id, step_execution_id) 
/*esta consulta agrega el observation_type time si el paso está terminado*/
select SE.time, 2, SE.id
from tpoodump.step S inner join tpoodump.step_execution SE on (S.id = SE.step_id)
where not question and result not like '%skip%';



