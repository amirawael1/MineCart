# Milestone 1: Literature Review and Data Analysis
## Amazon Product Question Answering System
### INCS 903 NLP Project - Winter 2025
### Amira Wael - Khaled Ehab
### December , 2025

---

## 1. Introduction

### 1.1 The Problem I Want to Solve
I'm writing this report as part of my Master's program in Natural Language Processing. For this project, I'm building a question answering system for Amazon products. The idea came from my own experience trying to shop online while studying. 

Last month, I needed to buy a new backpack for university. I spent hours on Amazon reading product descriptions, comparing prices, and trying to understand which one would be best for carrying my laptop and books. I kept thinking: "Why can't I just ask Amazon what I need and get a direct answer?" 

Current search systems only match keywords. If I search for "durable backpack for students," I get backpacks that happen to have those words in their descriptions. But what I really want is a system that understands my question and finds the best match based on actual features and reviews.

### 1.2 My Motivation
As a student, my time is limited. Between classes, assignments, and research, I don't have hours to spend shopping online. I also have a limited budget, so I need to make smart choices. A good question answering system could help students like me make better decisions faster.

From an academic perspective, this project lets me apply what I'm learning in my NLP courses. We study transformer models and question answering systems in class, but working with real Amazon data is different from textbook examples. This project helps me bridge the gap between theory and practice.

### 1.3 Project Objectives
My main goals are:

1. **Understand Amazon's product data structure** - How are products organized? What information is available?
2. **Build a neural network** that can answer questions about products
3. **Create something useful** that could actually help people shop better
4. **Learn practical NLP skills** that will help in my future career

### 1.4 Report Structure
This report has three main parts:
1. **Literature Review** - What I've learned about question answering systems
2. **Data Analysis** - Understanding the Amazon dataset
3. **Limitations and Next Steps** - Challenges I face and what comes next

## 2. Literature Review

### 2.1 Learning About QA Systems in Class
In my Natural Language Processing course this semester, we've been studying how computers understand and answer questions. The professor started with the basics and worked up to modern systems.

**Early Systems (2000s)**
The first question answering systems I learned about used simple rules. For example, if a question started with "Who is," the system would look for a person's name in the text. If it asked "When was," it would look for dates. These systems were limited because programmers had to write rules for every type of question.

I remember our first assignment: we had to create a simple QA system using regular expressions. Mine could answer questions like "What is the capital of France?" but only if the text said exactly "The capital of France is Paris." It broke if the wording was slightly different.

**Statistical Approaches (2010s)**
Next, we learned about machine learning approaches. Instead of writing rules, we could train models on examples. We used the Stanford Question Answering Dataset (SQuAD), which has questions and answers from Wikipedia articles.

For a class project, I built a system using TF-IDF (Term Frequency-Inverse Document Frequency). The idea was simple: find the sentence in a document that's most similar to the question. My system got about 60% of answers right. The professor explained this was decent for a simple approach but not good enough for real applications.

### 2.2 The Neural Network Revolution
The big change came when we started studying neural networks. This was the hardest but most interesting part of the course.

**Recurrent Neural Networks (RNNs)**
RNNs can process sequences of words. They read text word by word and remember what came before. We implemented a simple RNN for text classification. The challenge was that RNNs have trouble with long texts—they tend to "forget" the beginning by the time they reach the end.

**Long Short-Term Memory (LSTM) Networks**
LSTMs were designed to fix RNN's memory problem. They have special gates that decide what to remember and what to forget. For our midterm project, I built an LSTM-based QA system. It performed better than my TF-IDF system (about 70% accuracy) but took much longer to train.

### 2.3 Transformers and BERT
The most exciting part of the course was learning about transformers and BERT.

**The Transformer Architecture**
In 2017, researchers at Google published "Attention Is All You Need." They proposed a new architecture that didn't process words sequentially like RNNs. Instead, transformers use "attention" to look at all words in a sentence at once and understand how they relate to each other.

The professor showed us how attention works with a simple example: "The cat sat on the mat because it was tired." Which word does "it" refer to? Transformers can figure this out by looking at the relationships between all words.

**BERT: Bidirectional Encoder Representations from Transformers**
BERT, introduced in 2018, was a breakthrough. Previous models read text left-to-right (or right-to-left). BERT reads in both directions at once, which gives it better understanding of context.

What I found clever about BERT is its training method. During pre-training, it randomly hides 15% of words in a sentence and tries to predict them. For example, given "The [MASK] sat on the mat," it learns that "cat" is a good prediction. This "masked language modeling" teaches BERT about language patterns.

### 2.4 My Hands-On Experiments
After learning about these systems in class, I wanted to try them myself.

**Experiment 1: Using Pre-trained BERT**
Using Python's Hugging Face library, I tried a pre-trained BERT model:

```python
from transformers import pipeline

qa_pipeline = pipeline("question-answering")
result = qa_pipeline(
    question="Where was the 2022 World Cup held?",
    context="The 2022 FIFA World Cup was held in Qatar."
)
print(result['answer'])  # Output: Qatar

This worked surprisingly well with just a few lines of code. It made me realize how powerful pre-trained models are.

Experiment 2: Fine-tuning for Product Questions
I tried to fine-tune BERT on some Amazon data. I created 100 simple question-answer pairs like:

Q: "How much does this laptop cost?"

A: "The price is $899.99."

The model learned to answer price questions but struggled with more complex questions like "Which laptop is better for gaming?"

2.5 Research Papers I Read
For this project, I read several academic papers:

"BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding" (Devlin et al., 2019)

This is the original BERT paper

Key insight: Bidirectional training gives better language understanding

The authors tested on 11 different NLP tasks and achieved state-of-the-art results

"SQuAD: 100,000+ Questions for Machine Comprehension of Text" (Rajpurkar et al., 2016)

Introduced a large dataset for QA research

Created by having people read Wikipedia paragraphs and write questions

Became the standard benchmark for QA systems

"Attention Is All You Need" (Vaswani et al., 2017)

Introduced the transformer architecture

Showed that attention mechanisms alone could achieve good results

This paper changed the direction of NLP research

A survey on e-commerce NLP applications (2021)

Reviewed how NLP is used in online shopping

Covered recommendation systems, review analysis, and chatbots

Helped me understand the broader context of my project

2.6 The Gap I Found
Through my reading and experiments, I noticed something important: most QA research uses clean, structured datasets like Wikipedia articles. But real-world data—like Amazon product information—is messier. Products have incomplete descriptions, prices change frequently, and customer reviews vary in quality and length.

Few papers address how to build QA systems for e-commerce specifically. Most focus on general knowledge questions. This gap is what makes my project interesting and challenging.


**Save again (Ctrl+S)**

---

## 📊 **STEP 4: Write Data Analysis Section**

**Continue typing:**

```markdown
## 3. Data Analysis

### 3.1 About the Dataset
For this project, I'm using an Amazon product dataset from 2024. The full dataset contains 1.1 million products, but that's too large to process on my laptop. Instead, I'm working with a sample of 10,000 products that I selected randomly. This sample should represent the full dataset reasonably well.

The data comes in two files:
1. **Product information**: Includes title, price, reviews, category ID, and other details
2. **Category mapping**: Connects category IDs to category names

### 3.2 My Analysis Process
I used Python with several libraries:
- **pandas** for data manipulation
- **matplotlib** for creating charts
- **Jupyter Notebook** for interactive analysis

My analysis notebook (`notebooks/01_data_exploration.ipynb`) shows all the steps. I started by loading the data, checking for problems, then calculating statistics and creating visualizations.

### 3.3 What I Found

**Basic Statistics**
- **Total products analyzed**: 10,000
- **Number of categories**: 241 different categories
- **Average price**: $42.72
- **Most expensive product**: $1,395.00
- **Least expensive**: $0.00 (some free items)
- **Products marked as "best seller"**: 122 (about 1.2%)

**Price Distribution**
Prices vary widely, but most products are affordable:
- 25% of products cost less than $19.99
- 50% cost less than $29.99 (the median)
- 75% cost less than $49.99
- Only a few products cost hundreds of dollars

The average price is $42.72, but this is pulled up by some expensive items. The median ($29.99) better represents what a typical product costs.

**Category Analysis**
Products are spread across many categories. The most common ones are:

1. **Girls' Clothing**: 220 products (2.2% of the sample)
2. **Boys' Clothing**: 166 products (1.66%)
3. **Toys & Games**: 150 products (1.5%)
4. **Men's Shoes**: 148 products (1.48%)
5. **Girls' Jewelry**: 147 products (1.47%)

No single category dominates, which is good for my QA system—it needs to understand many types of products.

**Data Quality**
I checked for missing data and found:
- No missing prices
- No missing categories  
- All products have reviews
- The data seems complete and consistent

### 3.4 Visualizations
I created several charts to better understand the data:

1. **A histogram of prices** - Shows that most products cluster under $100
2. **A bar chart of top categories** - Visualizes which categories have the most products
3. **A box plot of prices** - Shows the distribution and outliers

These charts helped me spot patterns that weren't obvious from the numbers alone. For example, I can see that while most products are cheap, there's a long "tail" of expensive items.

### 3.5 What This Means for My QA System
The data analysis gives me confidence that:
1. **There's enough variety** - 241 categories means the system will need to understand different types of products
2. **Price information is complete** - I can answer price questions reliably
3. **Reviews are available** - I can use them to answer quality questions
4. **The data is clean** - I won't spend most of my time fixing data problems

However, I also see challenges:
1. **Price range is wide** - From free to $1,395 means the system needs to understand different price contexts
2. **Category imbalance** - Some categories have many products, others have few
3. **Real-world messiness** - Product titles aren't standardized, reviews vary in quality

## 4. Limitations and Challenges

### 4.1 Personal Limitations
I'm working on this project alone as a Master's student, which comes with constraints:

**Time Constraints**
I have other courses, assignments, and exams. I can dedicate about 10-15 hours per week to this project. The milestones are every two weeks, so I need to manage my time carefully.

**Hardware Limitations**  
My laptop has 16GB of RAM and no dedicated graphics card. This limits:
- How much data I can process at once
- The size of neural networks I can train
- How quickly I can experiment with different approaches

That's why I'm using a 10,000 product sample instead of the full 1.1 million products.

**Experience Level**
This is my first major NLP project. While I've done smaller assignments in class, building a complete system is more complex. I'm learning as I go, which means I might make mistakes or need to backtrack.

### 4.2 Dataset Limitations
**Sample Size Issue**
10,000 products is only 0.9% of the full dataset. While it's a statistically valid sample, rare product types might be missing or underrepresented.

**Time Sensitivity**
The data is from 2024. On Amazon, prices change frequently—sometimes daily during sales. A product that costs $50 in my dataset might cost $45 today or $55 tomorrow.

**Geographic Focus**
The data appears to be from Amazon US. Products, prices, and availability differ on Amazon sites in other countries. My system might not work as well for international users.

**Category Representation**
I used random sampling, which means some categories might be over- or under-represented. If I had more time, I would use stratified sampling to ensure each category is properly represented.

### 4.3 Technical Challenges
**Creating Training Data**
For my QA system to learn, I need examples of questions and correct answers. Creating these manually is time-consuming. I need to think of different ways people might ask about products and what good answers would be.

**Evaluating Quality**
How do I know if my system is working well? For factual questions like "What's the price?" I can check if the answer is correct. But for subjective questions like "Is this product good?" evaluation is harder.

**Handling Ambiguity**
Natural language is ambiguous. "Cheap" means different things for different products—a $50 phone might be cheap, but a $50 pencil would be expensive. The system needs to understand context.

**Scalability Concerns**
Even with 10,000 products, creating and training a QA system is computationally intensive. If this were a real system with millions of products and thousands of users, it would need to be much more efficient.

### 4.4 Ethical Considerations
**Bias in Data**
The dataset might reflect societal biases. For example, if certain products are marketed more to one gender, my system might learn those associations.

**Privacy Issues**
While I'm using publicly available product data, customer reviews might contain personal information. I need to be careful about how I handle this data.

**Commercial Use**
If this system were actually deployed on Amazon, it would need to be fair to all sellers and not favor certain products unfairly.

## 5. Conclusion and Next Steps

### 5.1 Summary of Findings
Through my literature review and data analysis, I've learned:

1. **Question answering has advanced dramatically** from simple rule-based systems to powerful transformer models like BERT.

2. **The Amazon dataset is suitable** for building a QA system—it has complete price information, diverse categories, and customer reviews.

3. **There are significant challenges** including computational limits, evaluation difficulties, and real-world data messiness.

4. **This project is feasible** within the semester timeline, though it will require careful planning and execution.

### 5.2 Confirmation of Project Direction
The data analysis confirms that I should proceed with my planned approach:

**Yes, I should use BERT or similar transformers** - They've proven effective for QA tasks.

**Yes, the data quality is sufficient** - No major data cleaning problems were found.

**Yes, the project scope is appropriate** - Challenging but achievable for a semester project.

### 5.3 Next Steps for Milestone 2
For the next milestone (due January 11), I will:

1. **Create training data** - Generate question-answer pairs from the product data
2. **Design the neural network architecture** - Start simple, then add complexity as needed
3. **Implement the model** - Write the code for training and inference
4. **Run initial experiments** - See how well the basic system works

Specifically, in the next two weeks I will:
- Write code to automatically generate QA pairs from product information
- Implement a simple neural network for QA
- Train it on a subset of my data
- Evaluate initial performance

### 5.4 Timeline Adjustment
Based on my analysis, I'm adjusting my timeline:

**Week 1 (Dec 21-28)**: Complete literature review and data analysis (this report)
**Week 2 (Dec 28-Jan 4)**: Create QA training dataset
**Week 3 (Jan 4-11)**: Implement and train initial model
**Week 4 (Jan 11-18)**: Evaluate and improve the model
**Week 5 (Jan 18-25)**: Fine-tune with pre-trained models (Milestone 3)
**Week 6 (Jan 25-Feb 1)**: Final evaluation and report

### 5.5 Personal Reflection
This first milestone has been valuable. I've:
- Deepened my understanding of QA systems
- Learned to work with real-world e-commerce data  
- Developed practical data analysis skills
- Gained clarity on the project's challenges and opportunities

The most important lesson: **real data is messier than textbook examples, but that's what makes it interesting.** Building a system that works in the real world requires dealing with imperfections and making practical compromises.

I'm looking forward to the next phase—actually building the QA system. The foundation is now solid, and I'm ready to start implementation.

---

## References

1. Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.

2. Rajpurkar, P., Zhang, J., Lopyrev, K., & Liang, P. (2016). SQuAD: 100,000+ Questions for Machine Comprehension of Text.

3. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... & Polosukhin, I. (2017). Attention is All You Need.

4. Course materials from INCS 903: Natural Language Processing, Winter 2025.

---

## Appendix

### A. Project Repository
All code and data are available at:  
https://github.com/amirawael1/nlp-amazon-qa-project

### B. Generated Files
The data analysis produced these files in the `reports/` folder:
- `milestone1_analysis_summary.csv` - Key statistics
- `category_distribution.csv` - Category counts
- `price_statistics.csv` - Price analysis
- `missing_values.csv` - Data completeness check

### C. Contact Information
**Student**: Amira Wael - Khaled Ehab  
**Email**: amira.wael@giu-uni.de  
**Course**: INCS 903 NLP Project  
**Institution**: German International University  
**Submission Date**: December, 2025



