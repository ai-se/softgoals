#!/usr/bin/env bash

array=('CSServices' 'CSCounselling' 'CSCounsellingManagement'
		#'CSCounsellingManagementSD' 'CSCounsellingSD'
		'CSFDandMarketing'
		#'CSFDandMarketingSD'
		'CSITDepartment' 'CSSAProgram' 'KidsAndYouth'
		#'Parents'
		#'OOOChatRooms' 'DelayModeratedBulletinBoard'
		)
#array=('OOOChatRooms' 'DelayModeratedBulletinBoard')
date='2016-09-06'
sub_folder='correction'
for i in ${array[*]}; do
	echo model: $i
#	python runner.py $i n > ../weekly-reports/$date/$sub_folder/$i.md
  python runner.py $i > txt_results/$i.md &
done