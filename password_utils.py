import math
import string

def calculate_entropy(password):
    charset = 0
    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(c in string.punctuation for c in password):
        charset += len(string.punctuation)
    return round(len(password) * math.log2(charset)) if charset > 0 else 0

def evaluate_password(password):
    entropy = calculate_entropy(password)
    
    length_score = len(password) >= 8
    upper_score = any(c.isupper() for c in password)
    digit_score = any(c.isdigit() for c in password)
    special_score = any(c in string.punctuation for c in password)

    total_score = sum([length_score, upper_score, digit_score, special_score])

    if total_score == 4 and entropy >= 60:
        return "Strong", entropy
    elif total_score >= 2 and entropy >= 40:
        return "Medium", entropy
    else:
        return "Weak", entropy
