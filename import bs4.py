import bs4

#리스트를 입력받고 평균을 계산하는 함수
def calculate_average(numbers):
    """
    리스트를 입력받아 평균을 계산하는 함수
    
    Args:
        numbers: 숫자들의 리스트
        
    Returns:
        float: 입력받은 숫자들의 평균
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# 사용 예시
if __name__ == "__main__":
    test_list = [10, 20, 30, 40, 50]
    result = calculate_average(test_list)
    print(f"평균: {result}")     
def average(lst):
    return sum(lst) / len(lst)              
