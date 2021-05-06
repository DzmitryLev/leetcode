if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()  

    # Add a var which holds the sum of student marks divided by 3, and print the answer with 2 decimal places after the dot.
    answer = (sum(student_marks[query_name]))/3 
    print("%.2f"%(answer))