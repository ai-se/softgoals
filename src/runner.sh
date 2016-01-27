#!/usr/bin/env bash

array=('CSServices' 'CSCounselling' 'CSCounsellingManagement' 'CSCounsellingManagementSD' 'CSCounsellingSD' 'CSFDandMarketing' 'CSFDandMarketingSD' 'CSITDepartment' 'CSSAProgram' 'CSSimplified' 'KidsAndYouth'
		#'Parents'
		'OOOChatRooms' 'DelayModeratedBulletinBoard'
		)
#array=('OOOChatRooms' 'DelayModeratedBulletinBoard')
sub_folder='minimals'
for i in ${array[*]}; do
	echo model: $i
	python runner.py $i y > ../weekly-reports/2016-01-27/$sub_folder/$i.md
done