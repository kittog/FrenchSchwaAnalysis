# Load required libraries
library(tidyverse)
library(cluster)
library(factoextra)
library(ggpubr)

# load data
data <- read_csv('data/results/schwa_analysis_results.csv')

print(head(data))

data_normalized <- data %>%
  mutate(across(duration:intensity, scale))

set.seed(123)
kmeans_result <- kmeans(data_normalized %>% select(duration:intensity), centers = 3)

data_normalized <- data_normalized %>%
  mutate(cluster = factor(kmeans_result$cluster))

# visualise the clusters
fviz_cluster(kmeans_result, data = data_normalized %>% select(duration:intensity),
             geom = "point", stand = FALSE, ellipse.type = "convex") +
  ggtitle("K-means Clustering of Schwa Intervals") +
  theme_minimal()

# save the clustered data
write_csv(data_normalized, 'data/results/schwa_clustered_results.csv')

# compare duration between pre-pausal and non-prepausal schwa using t-test
t_test_duration <- t.test(duration ~ label, data = data)
print(t_test_duration)

# plot duration comparison
duration_plot <- ggplot(data, aes(x = label, y = duration, fill = label)) +
  geom_boxplot() +
  labs(title = "Duration of Schwa: Pre-pausal vs. Non-prepausal", y = "Duration (s)") +
  theme_minimal()

ggsave("data/results/duration_comparison.png", duration_plot)

# ANOVA for duration, F1, F2, F0, intensity
anova_duration <- aov(duration ~ label, data = data)
summary(anova_duration)

anova_f1 <- aov(f1 ~ label, data = data)
summary(anova_f1)

anova_f2 <- aov(f2 ~ label, data = data)
summary(anova_f2)

anova_f0 <- aov(f0 ~ label, data = data)
summary(anova_f0)

anova_intensity <- aov(intensity ~ label, data = data)
summary(anova_intensity)

# plot formant frequencies
formant_plot <- ggplot(data, aes(x = f1, y = f2, color = label)) +
  geom_point(alpha = 0.7) +
  labs(title = "Formant Frequencies (F1 vs. F2) of Schwa", x = "F1 (Hz)", y = "F2 (Hz)") +
  theme_minimal()

ggsave("data/results/formant_frequencies.png", formant_plot)

# plot pitch
pitch_plot <- ggplot(data, aes(x = label, y = f0, fill = label)) +
  geom_boxplot() +
  labs(title = "Pitch (F0) of Schwa: Pre-pausal vs. Non-prepausal", y = "F0 (Hz)") +
  theme_minimal()

ggsave("data/results/pitch_comparison.png", pitch_plot)

# plot intensity
intensity_plot <- ggplot(data, aes(x = label, y = intensity, fill = label)) +
  geom_boxplot() +
  labs(title = "Intensity of Schwa: Pre-pausal vs. Non-prepausal", y = "Intensity (dB)") +
  theme_minimal()

ggsave("data/results/intensity_comparison.png", intensity_plot)

# save results
sink("data/results/statistical_summary.txt")
cat("T-test for Duration\n")
print(t_test_duration)

cat("\nANOVA for Duration\n")
print(summary(anova_duration))

cat("\nANOVA for F1\n")
print(summary(anova_f1))

cat("\nANOVA for F2\n")
print(summary(anova_f2))

cat("\nANOVA for F0\n")
print(summary(anova_f0))

cat("\nANOVA for Intensity\n")
print(summary(anova_intensity))
sink()
