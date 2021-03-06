from django.conf.urls import patterns, include, url

# custom management patterns
urlpatterns = patterns('core.views', 
	url(r'^payments/$', 'payments_today', name='location_payments_today'),
	url(r'^payments/(?P<year>\d+)/(?P<month>\d+)$', 'payments', name='location_payments'),
	url(r'reservations/$', 'ReservationManageList', name='reservation_manage_list'),
	url(r'reservation/(?P<reservation_id>\d+)/$', 'ReservationManage', name='reservation_manage'),
	url(r'reservation/(?P<reservation_id>\d+)/action/$', 'ReservationManageAction', name='reservation_manage_action'), 
	url(r'reservation/(?P<reservation_id>\d+)/payment/$', 'ReservationManagePayment', name='reservation_manage_payment'), 
	url(r'reservation/(?P<reservation_id>\d+)/togglecomp/$', 'ReservationToggleComp', name='reservation_toggle_comp'), 
	url(r'reservation/(?P<reservation_id>\d+)/addbillitem/$', 'ReservationAddBillLineItem', name='reservation_add_bill_item'), 
	url(r'reservation/(?P<reservation_id>\d+)/deletebillitem/$', 'ReservationDeleteBillLineItem', name='reservation_delete_bill_item'), 
	url(r'reservation/(?P<reservation_id>\d+)/sendreceipt/$', 'ReservationSendReceipt', name='reservation_send_receipt'), 
	url(r'reservation/(?P<reservation_id>\d+)/sendwelcome/$', 'ReservationSendWelcomeEmail', name='reservation_send_welcome'), 
	url(r'reservation/(?P<reservation_id>\d+)/sendmail/$', 'ReservationSendMail', name='reservation_send_mail'), 
	url(r'reservation/(?P<reservation_id>\d+)/recalculate/$', 'ReservationRecalculateBill', name='reservation_recalculate_bill'), 
	url(r'reservation/(?P<reservation_id>\d+)/edit/$', 'ReservationManageEdit', name='reservation_edit'), 
)


