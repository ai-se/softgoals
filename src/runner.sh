#!/usr/bin/env bash

array=('CSServices' 'CSCounselling' 'CSCounsellingManagement' 'CSCounsellingManagementSD' 'CSCounsellingSD' 'CSFDandMarketing' 'CSFDandMarketingSD' 'CSITDepartment' 'CSSAProgram' 'CSSimplified' 'KidsAndYouth'
		#'Parents'
		'OOOChatRooms' 'DelayModeratedBulletinBoard'
		)
#array=('OOOChatRooms' 'DelayModeratedBulletinBoard')
for  i in ${array[*]}; do
	echo model: $i
	python runner.py $i > ../weekly-reports/2015-12-24/unit_cost/$i.md
done