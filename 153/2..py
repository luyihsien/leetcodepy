#import datetime
#print(datetime.date(2019,8,31))
import calendar
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        d={0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
        cal = calendar.monthrange(year,month)
        return d[((day-1)%7+cal[0])%7]
print(Solution().dayOfTheWeek(day = 15, month = 8, year = 1993))