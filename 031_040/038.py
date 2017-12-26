# 038 문자열 분리 및 합치기
#
# 'spam egg' 문자열을 'egg samp'으로 변경하라.
str = 'spam egg'
str = str.split(' ')
print(str[1]+' '+str[0])