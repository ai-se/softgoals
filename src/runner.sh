#!/usr/bin/env bash

array=('CSServices' 'CSCounselling' 'CSCounsellingManagement' 'CSCounsellingManagementSD' 'CSCounsellingSD' 'CSFDandMarketing' 'CSFDandMarketingSD' 'CSITDepartment' 'CSSAProgram' 'CSSimplified' 'KidsAndYouth'
		#'Parents'
		'OOOChatRooms' 'DelayModeratedBulletinBoard'
		)
#array=('OOOChatRooms' 'DelayModeratedBulletinBoard')
sub_folder='even_smaller'
for i in ${array[*]}; do
	echo model: $i
	python runner.py $i y > ../weekly-reports/2016-01-28/$sub_folder/$i.md
done