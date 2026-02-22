def process_scores(students):
    res = {}

    for name, scores in students.items():
        if len(scores) == 0:
            avg = 0
        else:
            avg = sum(scores) / len(scores)

        res[name] = round(avg, 2)
    return res

def classify_grades(averages):
    res = {}
    for name, avg in averages.items():
        if avg >= 90:
            grade = "A"
        elif avg >= 75 and avg<90:
            grade = "B"
        elif avg >= 60 and avg<75:
            grade = "C"
        else:
            grade = "F"
        
        res[name] = (avg, grade)

    return res
  
def generate_report(classified, passing_avg=70):
  print("\n------- STUDENT GRADE REPORT -------\n")
  print(f"{'Name':<10} | {'Average':<10} | {'Grade':<6} | {'Status'}")
  print("-" * 40)

  pass_count = 0

  for name, (avg, grade) in classified.items():
      status = "Pass" if avg >= passing_avg else "Fail"
      if status == "Pass":
          pass_count += 1

      print(f"{name:<10} | {avg:<10} | {grade:<6} | {status}")

  print("-" * 40)
  print(f"Total Students :",len(classified))
  print(f"Passed         :", pass_count)
  print(f"Failed         :", len(classified) - pass_count)

  return pass_count  

students_data = {
        "Shivani": [85, 90, 78],
        "Rahul": [70, 75, 80],
        "Ananya": [60, 65, 58],
        "Kiran": [35, 40, 30],
        "Swathi": [95, 92, 98]
    }

averages = process_scores(students_data)
classified = classify_grades(averages)
total_passed = generate_report(classified)