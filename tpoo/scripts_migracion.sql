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
from tpoodump.refactorings

/*relacion entre scenario_task y refactoring -many to many, TODO en el modelo 
la relacion entre refactoring y appVersion vuela. Se reemplaza por metodo que hace las queries necesarias
*/
select task_version_id, refactoring_id
from(
select task_version_id, refactoring_id
from tpoodump.step
where refactoring_id is not null

UNION ALL

select task_version_id, second_refactoring_id
from tpoodump.step
where second_refactoring_id is not null

UNION ALL

select task_version_id, third_refactoring_id
from tpoodump.step
where third_refactoring_id is not null) T
group by task_version_id, refactoring_id



