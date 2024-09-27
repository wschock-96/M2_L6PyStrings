# TASK 1 KEYWORD HIGHLIGHTER

def caps_keywords(reviews, keywords):
    edited_reviews = []
    for review in reviews:
        for keyword in keywords:
            review = review.replace(keyword, keyword.upper())
        edited_reviews.append(review)
    return edited_reviews

while True:
    reviews = [
    "This product is really good . I'm impressed with its quality.",
    "The performance of this product is excellent . Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "A poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
    ]
    keywords = ["excellent", "good", "poor", "average", "bad"]
    edited_reviews = caps_keywords(reviews, keywords)

    for review in edited_reviews:
        print(review)
    else:
        break


# TASK 2 SENTIMENTAL TALLY

def num_of_words(pos_words, neg_words, reviews):
    positive_total = 0
    negative_total = 0 
    
    for review in reviews:
        words = review.split()
        for word in words:
                if word in pos_words:
                    positive_total += 1
                elif word in neg_words:
                    negative_total += 1

    return f"Total number of positive: {positive_total}", f"Total number of negative: {negative_total}"
        

while True:
    pos_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    neg_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
     
    num_of_pos, num_of_neg = num_of_words(pos_words, neg_words, reviews)

    print(num_of_pos)
    print(num_of_neg)
    break



# TASK 3 REVIEW SUMMARY

def review_summary(review, line_length = 30):
    summaries = []

    for review in reviews:
        if len(review) <= line_length:
            summaries.append(review)
        else:
            cut_review = review[:line_length]
            last_space = cut_review.rfind(' ')

            if last_space != -1:
                summary = cut_review[:last_space]
            else:
                summary = cut_review
            
            summaries.append(summary + '...')

    return summaries

while True:
    summaries = review_summary(reviews)
    for summary in summaries:
        print(summary)
    break

