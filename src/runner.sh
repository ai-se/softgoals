#!/usr/bin/env bash

array=('CSServices' 'CSCounselling' 'CSCounsellingManagement' 'CSCounsellingManagementSD' 'CSCounsellingSD' 'CSFDandMarketing' 'CSFDandMarketingSD' 'CSITDepartment' 'CSSAProgram' 'CSSimplified' 'KidsAndYouth'
		#'Parents'
		'OOOChatRooms' 'DelayModeratedBulletinBoard'
		)
#array=('OOOChatRooms' 'DelayModeratedBulletinBoard')
date='2016-01-30'
sub_folder='cdom'
for i in ${array[*]}; do
	echo model: $i
	python runner.py $i y > ../weekly-reports/$date/$sub_folder/$i.md
done