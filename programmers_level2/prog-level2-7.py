# https://programmers.co.kr/learn/courses/30/lessons/49993\
# 스킬트리

def solution(skill, skill_trees):
    """ 스킬순서 리스트에서 역순으로 원소를 꺼내서 확인 합니다."""
    """ 'CBD'라면 D를 찾고, D가 있으면 B가 반드시 있어야 합니다. B가 있으면 C가 반드시 있어야 합니다. """
    count = 0   # 가능한 스킬트리 개수
    
    # skill_trees에서 skill_tree를 하나씩 가져와서 확인
    for skill_tree in skill_trees:
        n = len(skill)
        t = len(skill_tree)     # 선행스킬은 앞에 위치 하므로 t는 검색 범위를 좁히기 위한 끝 인덱스. 
        chk = 0                 # 찾는 스킬이 skill_tree에 있으면 카운트
        k = -1                  # skill 역순으로 찾기 위한 인덱스 -1씩 감소
        idx = 0
        while n > 0:
            idx = skill_tree.find(skill[k])     # 찾는 스킬 인덱스를 idx에 참조
            if chk > 0 and idx == -1:           # 스킬을 찾았는데 선행스킬이 없으면 break
                break
            if 0 <= idx < t:
                chk += 1
                t = idx    
            elif idx > t:                       # 선행스킬이 뒤에 위치하면 break
                idx = -1
                break
            k -= 1        
            n -= 1
        
        if chk > 0 and idx == -1:
            continue
        count += 1      # skill_tree에서 skill을 전혀 찾을 수 없거나(chk =0, idx = -1) 가능한 스킬트리면 count합니다.     

    return count