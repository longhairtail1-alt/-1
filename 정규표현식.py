
import re

# 문서 읽기
with open("07-02. 전주대 대동제 및 해커톤 통합운영 데이터 로그.txt",
          "r", encoding="utf-8") as f:
    text = f.read()


# 1. 유효한 이메일 추출
emails = re.findall(
    r'(?<![\w.+-])[\w.+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+(?![\w.-])',
    text
)

print("1. 유효한 이메일")
for email in emails:
    print(email)


# 2. 휴대폰 번호 추출
phones = re.findall(
    r'(?<!\d)010(?:[-.\s]?\d{4}){2}(?!\d)',
    text
)

print("\n2. 휴대폰 번호")
for phone in phones:
    print(phone)


# 3. 학번과 학과 추출
students = re.findall(
    r'\[(202\d{6})\s*/\s*([^\]]+)\]',
    text
)

print("\n3. 학번과 학과")
for student in students:
    print(student)


# 4. GitHub 주소 및 2026년 쿠폰 추출
github = re.findall(
    r'https?://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(?:\.git)?',
    text
)

coupons = re.findall(
    r'FEST-2026-[A-Z0-9]{4}',
    text
)

print("\n4. GitHub 저장소 주소")
for url in github:
    print(url)

print("\n2026년 유효 쿠폰")
for coupon in coupons:
    print(coupon)


# 5. 부스별 매출 추출 및 총합 계산
sales = re.findall(
    r'매출\s*:\s*([\d,]+)\s*원',
    text
)

total = 0

print("\n5. 부스별 매출")

for amount in sales:
    price = int(amount.replace(",", ""))
    total += price
    print(f"{price:,}원")

print(f"\n전체 매출 합계: {total:,}원")
