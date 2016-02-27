#!/usr/bin/env bash

array=('CSServices' 'CSCounselling' 'CSCounsellingManagement'
		#'CSCounsellingManagementSD' 'CSCounsellingSD'
		'CSFDandMarketing'
		#'CSFDandMarketingSD'
		'CSITDepartment' 'CSSAProgram' 'CSSimplified' 'KidsAndYouth'
		#'Parents'
		#'OOOChatRooms' 'DelayModeratedBulletinBoard'
		)
#array=('OOOChatRooms' 'DelayModeratedBulletinBoard')
date='2016-02-27'
sub_folder='induced_softgoals'
for i in ${array[*]}; do
	echo model: $i
	python runner.py $i n > ../weekly-reports/$date/$sub_folder/$i.md
done