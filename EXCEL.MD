prompt Importing table pes_txn_handler_def...
set feedback off
set define off
insert into pes_txn_handler_def (SID, HANDLER_NAME, HANDLER_DESC, HANDLER_ID, CREATED_BY, CREATED_DT, UPDATED_BY, UPDATED_DT, VERSION)
values (",A1,", '",B1,"', '",C1,"', '",D1,"', 'sgc', to_date('23-08-2018', 'dd-mm-yyyy'), null, null, 1);

prompt Done.


=CONCATENATE("insert into pes_txn_handler_def (SID, HANDLER_NAME, HANDLER_DESC, HANDLER_ID, CREATED_BY, CREATED_DT, UPDATED_BY, UPDATED_DT, VERSION) values (",A1,", '",B1,"', '",C1,"', '",D1,"', 'sgc', to_date('23-08-2018', 'dd-mm-yyyy'), null, null, 1);")


insert into pes_txn_handler_def (SID, HANDLER_NAME, HANDLER_DESC, HANDLER_ID, CREATED_BY, CREATED_DT, UPDATED_BY, UPDATED_DT, VERSION) values (1020, 'TXN_QM_L10181059H1_HANDLER', '热轧物料信息同步-管理封锁处理Handler', 'l10181059H1Handler', 'sgc', to_date('23-08-2018', 'dd-mm-yyyy'), null, null, 1);
insert into pes_txn_handler_def (SID, HANDLER_NAME, HANDLER_DESC, HANDLER_ID, CREATED_BY, CREATED_DT, UPDATED_BY, UPDATED_DT, VERSION) values (1021, 'TXN_QM_L10181059H2_HANDLER', '热轧物料信息同步-管理释放处理Handler', 'l10181059H2Handler', 'sgc', to_date('23-08-2018', 'dd-mm-yyyy'), null, null, 1);
insert into pes_txn_handler_def (SID, HANDLER_NAME, HANDLER_DESC, HANDLER_ID, CREATED_BY, CREATED_DT, UPDATED_BY, UPDATED_DT, VERSION) values (1022, 'TXN_QM_L10181059HE_HANDLER', '热轧物料信息倒灌处理Handler', 'l10181059HEHandler', 'sgc', to_date('23-08-2018', 'dd-mm-yyyy'), null, null, 1);
insert into pes_txn_handler_def (SID, HANDLER_NAME, HANDLER_DESC, HANDLER_ID, CREATED_BY, CREATED_DT, UPDATED_BY, UPDATED_DT, VERSION) values (1023, 'TXN_QM_L10181059HF_HANDLER', '热轧表面缺陷信息倒灌电文处理Handler', 'l10181059HFHandler', 'sgc', to_date('23-08-2018', 'dd-mm-yyyy'), null, null, 1);
insert into pes_txn_handler_def (SID, HANDLER_NAME, HANDLER_DESC, HANDLER_ID, CREATED_BY, CREATED_DT, UPDATED_BY, UPDATED_DT, VERSION) values (1024, 'TXN_QM_L10181059Q1_HANDLER', '热轧质量管理处置电文处理Handler', 'l10181059Q1Handler', 'sgc', to_date('23-08-2018', 'dd-mm-yyyy'), null, null, 1);
insert into pes_txn_handler_def (SID, HANDLER_NAME, HANDLER_DESC, HANDLER_ID, CREATED_BY, CREATED_DT, UPDATED_BY, UPDATED_DT, VERSION) values (1025, 'TXN_QM_L10181059Q3_HANDLER', '热轧取样委托电文处理Handler', 'l10181059Q3Handler', 'sgc', to_date('23-08-2018', 'dd-mm-yyyy'), null, null, 1);
insert into pes_txn_handler_def (SID, HANDLER_NAME, HANDLER_DESC, HANDLER_ID, CREATED_BY, CREATED_DT, UPDATED_BY, UPDATED_DT, VERSION) values (1026, 'TXN_QM_L10181059Q4_HANDLER', '热轧出钢标记信息处理Handler', 'l10181059Q4Handler', 'sgc', to_date('23-08-2018', 'dd-mm-yyyy'), null, null, 1);
insert into pes_txn_handler_def (SID, HANDLER_NAME, HANDLER_DESC, HANDLER_ID, CREATED_BY, CREATED_DT, UPDATED_BY, UPDATED_DT, VERSION) values (1027, 'TXN_QM_L10591018HO_HANDLER', '表面缺陷实绩发送电文', 'l10591018HOHandler', 'sgc', to_date('23-08-2018', 'dd-mm-yyyy'), null, null, 1);
insert into pes_txn_handler_def (SID, HANDLER_NAME, HANDLER_DESC, HANDLER_ID, CREATED_BY, CREATED_DT, UPDATED_BY, UPDATED_DT, VERSION) values (1028, 'TXN_QM_L10591018HR_HANDLER', '停机实绩发送电文公共类', 'l10591018HRHandler', 'sgc', to_date('23-08-2018', 'dd-mm-yyyy'), null, null, 1);
insert into pes_txn_handler_def (SID, HANDLER_NAME, HANDLER_DESC, HANDLER_ID, CREATED_BY, CREATED_DT, UPDATED_BY, UPDATED_DT, VERSION) values (1029, 'TXN_QM_L1023105901_HANDLER', '一贯冷轧封闭电文处理Handler', 'l1023105901Handler', 'sgc', to_date('23-08-2018', 'dd-mm-yyyy'), null, null, 1);
insert into pes_txn_handler_def (SID, HANDLER_NAME, HANDLER_DESC, HANDLER_ID, CREATED_BY, CREATED_DT, UPDATED_BY, UPDATED_DT, VERSION) values (1030, 'TXN_QM_L1023105902_HANDLER', '一贯冷轧处置电文处理Handler ', 'l1023105902Handler', 'sgc', to_date('23-08-2018', 'dd-mm-yyyy'), null, null, 1);
insert into pes_txn_handler_def (SID, HANDLER_NAME, HANDLER_DESC, HANDLER_ID, CREATED_BY, CREATED_DT, UPDATED_BY, UPDATED_DT, VERSION) values (1031, 'TXN_QM_L1023105903_HANDLER', '一贯热轧缺陷实绩电文', 'l1023105903Handler', 'sgc', to_date('23-08-2018', 'dd-mm-yyyy'), null, null, 1);




create or replace view view_pdo_hotrolling_performance as
select
	M.mat_id,
	max(decode(pdo.attr_name,'slabId',pdo.attr_value,null))   mat_no  ,
	max(decode(pdo.attr_name,'coilId',pdo.attr_value,null))   COIL_NO  ,
	max(decode(pdo.attr_name,'PROD_SHIFT_NO',pdo.attr_value,null))   PROD_SHIFT_GROUP  ,
	max(decode(pdo.attr_name,'PROD_SHIFT_NO',pdo.attr_value,null))   PROD_SHIFT_NO  ,
	max(decode(pdo.attr_name,'MAT_ACT_WIDTH',pdo.attr_value,null))   MAT_ACT_WIDTH  ,
	max(decode(pdo.attr_name,'MAT_ACT_THICK',pdo.attr_value,null))   MAT_ACT_THICK  ,
	max(decode(pdo.attr_name,'coilLength',pdo.attr_value,null))   MAT_LEN  ,
	max(decode(pdo.attr_name,'steelGradeCode',pdo.attr_value,null))   STEEL_CODE  ,
	max(decode(pdo.attr_name,'slabLength',pdo.attr_value,null))   coilLength  ,
	max(decode(pdo.attr_name,'TimeofActualStripreachF1',pdo.attr_value,null))   RollingStartDateAndTime  ,
	max(decode(pdo.attr_name,'TimeofActualStripleaveF7',pdo.attr_value,null))   rollingCompletionDateandTime  ,
	'' DEAL_FLAG,
	'' plan_fur_mode,
	'' factory_div,
	'' UNIT_CODE,
	'' CHARGE_SHIFT_GROUP,
	'' CHARGE_SHIFT_NO,
	'' ,
	'' PLAN_NO,
	'' ,
	'' CHARGE_TIME,
	'' FUR_NO,
	'' DISCHARGE_TEMP_ACT,
	'' DISCHARGE_SHIFT_NO,
	'' DISCH_TIME,
	'' IN_FUR_PRED,
	'' CHARGE_TEMP_ACT,
	'' DISCH_TEMP_ACT,
	'' soakingSectionTemperature,
	'' CHARGE_SLAB_WT,
	'' PROD_CODE,
	'' PROD_CNAME,
	'' PROD_CLASS_CODE,
	'' PROD_CLASS_DESC,
	'' ST_NO,
	'' SG_SIGN,
	'' SG_SIGN,
	'' STD_SG_CODE,
	'' steel_code_desc,
	'' ORDER_NO,
	'' ORDER_THICK,
	'' ORDER_WIDTH,
	'' MAT_ACT_WT,
	'' SAMPLE_LOT_NO,
	'' COIL_WEIGHT_CALC
from pes_mat_material m
left join  pes_mat_pdo_attr_value pdo
on m.mat_id=pdo.mat_id
group by M.mat_id,M.YIELD_EQPT_ID;