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
