
# coding: utf-8

# # Test a Perceptual Phenomenon
# 
# by _**Ashish Sahu**_ (May, 2017)

# ### Stroop Effect (Information)
# 
# In a Stroop task, participants are presented with a list of words, with each word displayed in a color of ink. The participant’s task is to say out loud the color of the ink in which the word is printed. The task has two conditions: a congruent words condition, and an incongruent words condition. In the congruent words condition, the words being displayed are color words whose names match the colors in which they are printed: for example RED, BLUE. In the incongruent words condition, the words displayed are color words whose names do not match the colors in which they are printed: for example PURPLE, ORANGE. In each case, we measure the time it takes to name the ink colors in equally-sized lists. Each participant will go through and record a time from each condition.
# 
# **Reference:** [Wikipedia- Stroop Effect](https://en.wikipedia.org/wiki/Stroop_effect)

# ### Investigation

# ** 1. What is our independent variable? What is our dependent variable?**
# 
# * **Independent Variable:** The word-color condition (congruent words or incongruent words).
# * **Dependent variable:** The time it takes to recognize/name the ink colors of the mismatch word/colour congruency.

# ** 2. What is an appropriate set of hypotheses for this task? What kind of statistical test do you expect to perform? Justify your choices.**
# 
# * **Null Hypothesis, H0:** -  The mismatch of color to word will have no effect or decreased time to recognize and say the color
# * **Alternate Hypothesis, Ha: ** - The mismatch of color and word will increase time to recognize and say the color.
# 
# * H0: μc ≤ μi
# * H1: μc < μi
# 
# where μi = Incogruent words mean time to recognize and μc = Cogruent words mean time to recognize
# 
# * **Statistical Test**: - Paired One tail t-test. 
# 
# It is a t-test instead of z-test, because the population variance and standard deviation is unknown, sample size is less than 30. Also the same subject is exposed to two conditions and tested for each, which are the defining criteria for "repeated-measures" statistical tests, which implies that it should be **dependent sample** test. I would do one tail t-test in postive direction.
# 
# **Reference:** [Stat Trek - t distribution](http://stattrek.com/probability-distributions/t-distribution.aspx)

# ** 3. Report some descriptive statistics regarding this dataset. Include at least one measure of central tendency and at least one measure of variability.**

# In[3]:

# import necessory libraries to read, describe

import csv
import numpy as np
import pandas as pd

stroopdata = pd.read_csv("stroopdata.csv")
stroopdata.head()


# In[4]:

# add a column to dataset named as 'Difference'
stroopdata['Difference'] = stroopdata.Incongruent - stroopdata.Congruent
stroopdata.describe()


# **Congruent Dataset:**
# * Mean = 14.05
# * Median = 14.36
# * SD = 3.56
# 
# **Incongruent Dataset:**
# * Mean = 22.02
# * Median = 21.02
# * SD = 4.79
# 
# **Difference:**
# * Diff-Mean = 7.97
# * Diff-SD = 4.86
# 
# **[Standard-Error](http://stattrek.com/estimation/standard-error.aspx?Tutorial=AP)** = 0.993
# 
# **Reference:** [Central Tendency](https://statistics.laerd.com/statistical-guides/measures-central-tendency-mean-mode-median.php) and [Variability](http://www.statisticshowto.com/variability)

# ** 5. Provide one or two visualizations that show the distribution of the sample data. Write one or two sentences noting what you observe about the plot or plots.**

# In[5]:

# import visualisation libraries

import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')

# Seaborn for visualisation
import seaborn as sns
sns.distplot(stroopdata.Incongruent, bins=10, axlabel = 'Congruent Density-Histrogram', color='Red')


# In[6]:

# Time-spread of the Congruent words
sns.boxplot(stroopdata.Incongruent, color='cyan', orient='v')


# In[10]:

# Recognition time (Seconds) - X-axis
plt.hist(x=[stroopdata.Congruent, stroopdata.Incongruent], stacked=False, bins=20)


# ** 5. Perform the statistical test and report your results. What is your confidence level and your critical statistic value? Do you reject the null hypothesis or fail to reject it? Come to a conclusion in terms of the experiment task. Did the results match up with your expectations?**

# I'm going to perform the statistical test at the 95% confidence level (α = .05) with 23 degrees of freedom.
# 
# * _df_ = 23
# * _Aalpha_ = 0.05
# * _t-score_ = 8.021
# * _t-ctritical values_ = 1.714
# * _Confidence Intervals_ = 5.29 and 10.63
# * _P-value_ =< 0.0001
# 
# At 95% confidence level and 23 degrees of freedom, our p value is way less than alpha (0.05), Since the t-score falls in the critical region we reject the null hypothesis. We can safely say that congruent and incongreunt time are very different and we can draw conclusion that **word-color mismatch does have an impact on participant's reading time response and ovweall perception.**
# 
# **Reference:** [t-table](http://faculty.washington.edu/heagerty/Books/Biostatistics/TABLES/t-Tables/) and [P-value](http://www.graphpad.com/quickcalcs/distMenu/)

# ** 6. What do you think is responsible for the effects observed? Can you think of an alternative or similar task that would result in a similar effect? Some research about the problem will be helpful for thinking about these two questions!**

# * Pcychologically, way our brain receives causes a problem, which draws  interference between the different information wchich is what the words say and what is the color of the words. The effect is related to the ability of most people to read words more   quickly and automatically than they can name colors. Color-words mismatch require selective attention, and slows down humans Speed-Processing capabilty.
# 
# * Another nice experiment would be flipping the words and recording the response time, checking comparing normal people's congruent word response time to a color-blind person reading response.

# In[ ]:



