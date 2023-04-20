# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 18:11:01 2023

@author: 산업인공지능학 2023254003 윤재호
"""

import durable_rules_engine 
from durable.lang import *

with ruleset('Process'):
    # Rule 1 영업팀에서 수주를 접수하면 수주등록을 한다
    @when_all(s.status == 'receipt_of_orders')
    def receipt_of_orders(c):
        c.s.status = 'order_registration' 
        print('Process#1 Register to receive an order')

    # Rule 2 수주등록을 하면 생산팀에서 생산계획을 수립을 한다
    @when_all(s.status == 'order_registration')
    def order_registration(c):
        c.s.status = 'production_Planning' 
        print('Process#2 The production team establishes a production plan')

    # Rule 3 생산계획이 수립되면 자재팀에서 자재 발주를 한다
    @when_all(s.status == 'production_Planning')
    def production_Planning(c):
        c.s.status = 'material_orders'
        print('Process#3 Materials team places an order for materials')
        
    # Rule 4 자재팀에서 자재발주를 하면 외주 자재가 입고된다     
    @when_all(s.status == 'material_orders')
    def material_orders(c):
        c.s.status = 'material_input'
        print('Process#4 Outsourced materials are received')
        
    # Rule 5 외주 자재가 입고되면 품질팀에서 입고검사를 한다   
    @when_all(s.status == 'material_input')
    def material_input(c):
        c.s.status = 'import_inspection'
        print('Process#5 Inspection by quality teamn')
     
    # Rule 6 입고검사가 합격이면 자재입고 등록을 한다
    @when_all(s.status == 'import_inspection')
    def import_inspection(c):
        c.s.status = 'material_registration'
        print('Process#6 Register material warehousing')          
        
    # Rule 7 입고된 자재를 준비하면 패널 생산을 준비한다
    @when_all(s.status == 'material_registration')
    def material_registration(c):
        c.s.status = 'production_preparation'
        print('Process#7 Prepare for panel production')
        
    # Rule 8 생산 준비가 완료되면 패널 초품 생산을 시작한다    
    @when_all(s.status == 'production_preparation')
    def production_preparation(c):
        c.s.status = 'first_production'
        print('Process#8 Beginning of initial production')
        
    # Rule 9 패널 초품 생산을 시작하면 품질팀에서 공정검사를 진행한다
    @when_all(s.status == 'first_production')
    def first_production(c):
        c.s.status = 'process_inspection'
        print('Process#9 Process inspection by the quality team')
        
    # Rule 10 품질팀 공정검사가 합격이면 패널 양산생산을 한다
    @when_all(s.status == 'process_inspection')
    def process_inspection(c):
        c.s.status = 'mass_production'
        print('Process#10 Do panel production')
         
    # Rule 11 패널 양산생산 하면 품질팀에서 제품 검사를 실시한다
    @when_all(s.status == 'mass_production')
    def mass_production(c):
        c.s.status = 'product_inspection'
        print('Process#11 Product inspection')
         
    # Rule 12 품질팀 제품검사가 합격이면 패널 제품을 포장을 한다
    @when_all(s.status == 'product_inspection')
    def product_inspection(c):
        c.s.status = 'product_packaging'
        print('Process#12 Packaging of panel products')
         
    # Rule 13 패널 제품이 포장이 완료되면 야적장에 보관한다
    @when_all(s.status == 'product_packaging')
    def product_packaging(c):
        c.s.status = 'storage_in_the_yard'
        print('Process#13 Keep in the yard')

    # Rule 14 야적장에 보관되면 출고팀에서 출고 배차를 한다
    @when_all(s.status == 'storage_in_the_yard')
    def storage_in_the_yard(c):
        c.s.status = 'ready_to_ship'
        print('Process#14 Prepares for delivery')
           
    # Rule 15 출고 배차를 하면 거래명세표를 발행한다
    @when_all(s.status == 'ready_to_ship')
    def ready_to_ship(c):
        c.s.status = 'issuance_of_transaction_details'
        print('Process#15 Issue a transaction statement')
         
    # Rule 16 거래명세표가 발행되면 영업관리팀에서 출고서류를 준비한다
    @when_all(s.status == 'issuance_of_transaction_details')
    def issuance_of_transaction_details(c):
        c.s.status = 'prepare_release_documents'
        print('Process#16 Issuance of release documents')
         
    # Rule 17 출고서류가 준비되면 품질팀에서 품질확인서를 발행한다
    @when_all(s.status == 'prepare_release_documents')
    def prepare_release_documents(c):
        c.s.status = 'issuance_of_quality_certificate'
        print('Process#17 Issuance of quality certificate')
         
    # Rule 18 품질확인서가 발행되면 한국건설기술연구원에 품질확인서를 등록한다 
    @when_all(s.status == 'issuance_of_quality_certificate')
    def issuance_of_quality_certificate(c):
        c.s.status = 'registration_of_quality_certificate' 
        print('Process#18 Register quality certificate')
         
    # Rule 19 품질확인서 등록을 확인하면 패널제품을 출하한다
    @when_all(s.status == 'registration_of_quality_certificate')
    def registration_of_quality_certificate(c):
        c.s.status = 'shipment_of_panel_products'
        print('Process#19 Shipment of panel products')

    # Rule 20 패널 제품이 출하되면 납품처에 입고 확인을 받는다
    @when_all(s.status == 'shipment_of_panel_products')
    def shipment_of_panel_products(c):
        c.s.status = 'confirmation_of_delivery_destination'
        print('Process#20 Receive confirmation from the suppliers')

    # Rule 21 납품처의 확인을 받으면 세금계산서를 발행한다
    @when_all(s.status == 'confirmation_of_delivery_destination')
    def confirmation_of_delivery_destination(c):
        c.s.status = 'end'
        print('Process#21 Issue a tax invoice')
        c.delete_state()

    
# 생산 process에서 현재 공정이 주어지면 주어진 규칙에 따라 진행해야 할 공정 출력하여 공정 누락을 개선
update_state('Process', { 'status': 'material_orders' })
print('--------------------------------------------------------------------')
update_state('Process', { 'status': 'issuance_of_transaction_details' })
print('--------------------------------------------------------------------')
update_state('Process', { 'status': 'product_packaging' })




