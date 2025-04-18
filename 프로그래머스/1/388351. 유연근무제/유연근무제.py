# 월 화 수 목 금 토 일
# 0  1  2  3  4 5  6
def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(timelogs)):
        print(i,'번째 사원 확인중 .. . . . ')
        # i 번째 직원의 타임로그
        timelog = timelogs[i]
        duetime = schedules[i]
        
        duetimeHour = duetime // 100
        duetimeMin = duetime % 100
        
        duetime = duetimeHour*60 + duetimeMin + 10
        
        flag = True
        
        
        day = startday - 1
        
        for time in timelog:
            
    
            timeHour = time // 100
            timeMin = time  % 100
            
            time = timeHour* 60 + timeMin
            
            #print('요일 : ',day, '출근시각 ', timeHour , timeMin, '제한 시간 : ',duetime)
            if time > duetime and day!= 5 and day != 6:
                flag = False
            
            day+=1
            day%=7
            
        if flag:
            answer+=1
            
    return answer