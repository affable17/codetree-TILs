OFFSET = 11

N = int(input())
segment = [tuple(input().split()) for _ in range(N)]
start =0
end = 0
arr =[0]*21

#steps 표시해주기
for xL, xR in segment:
    start = end 
    if xR == 'R':
        end += int(xL)
    else: #xR == 'L'
        end -= int(xL)
    
    new_st = start + OFFSET
    new_ed = end + OFFSET
    if new_st > new_ed:
        new_st, new_ed = new_ed, new_st
    for i in range(new_st, new_ed):
        arr[i]+=1            

cnt =0
for j in range(len(arr)):
    if arr[j]>=2:
        cnt+=1
print(cnt)