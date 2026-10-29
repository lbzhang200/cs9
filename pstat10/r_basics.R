# =====================================================================
#  R BASICS — catch-up file (PSTAT 10, weeks 1–3 + a bit ahead)
#
#  HOW TO USE:
#   - Open in VS Code, put your cursor on a line, press Cmd+Enter to run it
#     (or run everything:  Rscript r_basics.R  from the terminal)
#   - Read the comment, GUESS the output, then run and check.
#   - Uses only base R + built-in datasets, so nothing to install.
#   - Practice problems at the bottom, answers below them.
# =====================================================================


# ---------------------------------------------------------------------
# 1. R AS A CALCULATOR + ASSIGNMENT
# ---------------------------------------------------------------------
2 + 2
100 * 3
100 / 10
7 %/% 2        # integer division  -> 3
7 %% 2         # modulus (remainder) -> 1   (even/odd checks!)
2^10           # power
sqrt(25)
abs(-4)
round(3.14159, 2)

y <- 3                 # "<-" is assignment (= also works, but use <-)
y_cube <- y^3
y_cube
(z <- 10)              # wrapping in () assigns AND prints

# R is case-sensitive:  y_cube exists, Y_CUBE does not
# Names can't start with a number:  2sq <- 4  is an error


# ---------------------------------------------------------------------
# 2. DATA TYPES
# ---------------------------------------------------------------------
typeof("Ally")    # "character"
typeof(1)         # "double"   (numbers are doubles by default)
typeof(1L)        # "integer"  (L forces integer)
typeof(TRUE)      # "logical"

5 < 9             # comparisons give logicals
5 == 5            # equality is ==   (= is assignment!)
5 != 4            # not equal
TRUE & FALSE      # and
TRUE | FALSE      # or
!TRUE             # not

# Coercion: converting types
as.integer(3.9)       # 3   (truncates, doesn't round)
as.character(42)      # "42"
as.numeric("3.5")     # 3.5
as.numeric("hello")   # NA with a warning
as.numeric(TRUE)      # 1
TRUE + TRUE           # 2   (TRUE counts as 1, FALSE as 0)
as.logical(0)         # FALSE  (any nonzero number -> TRUE)

class(3)              # "numeric"  (class is the "user-facing" type)


# ---------------------------------------------------------------------
# 3. VECTORS  (the most important thing in R)
#    A vector holds values that are ALL the same type.
# ---------------------------------------------------------------------
a <- c(1, 6, 5.3, 6, -2, 4)                       # numeric
students <- c("Maribel", "Evelyn", "David")       # character
met_OH <- c(FALSE, TRUE, TRUE)                    # logical

length(a)
sort(a)                    # sorted COPY, a itself is unchanged
sort(a, decreasing = TRUE)
a                          # still unsorted
rev(a)                     # reversed
sum(a); mean(a); median(a); max(a); min(a)
which.max(a)               # POSITION of the max (index), not the value
range(a)
sd(a); var(a)              # standard deviation, variance

# Mixing types -> everything gets coerced to the most general type
c(1, "two", TRUE)          # all become character!
c(1, TRUE, FALSE)          # all become numeric: 1 1 0

# Fast ways to make vectors
1:10
10:1
seq(from = 0, to = 1, by = 0.25)
seq(1, 10, length.out = 4)
rep(5, times = 3)                 # 5 5 5
rep(c("a", "b"), times = 2)       # a b a b
rep(1:3, each = 2)                # 1 1 2 2 3 3

# Vectorized math: works element-by-element, no loop needed
x <- c(1, 2, 3)
x * 10
x + c(10, 20, 30)
x^2
sqrt(x)
x > 1                      # TRUE/FALSE for each element


# ---------------------------------------------------------------------
# 4. INDEXING + FILTERING VECTORS   (R starts counting at 1!)
# ---------------------------------------------------------------------
x <- c(1, 7, 3, 10, 5)
x[1]            # first element
x[4]            # fourth
x[length(x)]    # last
x[-2]           # everything EXCEPT the 2nd
x[1:3]          # first three
x[c(1, 3)]      # 1st and 3rd
x[4] <- 100     # update an element
x

# Filtering with a logical condition (super common!)
price <- c(500, -10, 30, 20, -10, -3, -2, 100, 90)
price > 0                 # logical vector
price[price > 0]          # keep only positive
price[price > 0 & price < 100]
sum(price > 0)            # COUNT of positives (TRUE = 1)
mean(price > 0)           # PROPORTION positive
which(price < 0)          # positions of negatives

# Named vectors
scores <- c(alice = 90, bob = 75, carol = 88)
scores["bob"]
names(scores)
scores[scores > 80]


# ---------------------------------------------------------------------
# 5. MISSING VALUES (NA)
# ---------------------------------------------------------------------
v <- c(4, NA, 7, 1)
mean(v)                  # NA  — one NA poisons the result
mean(v, na.rm = TRUE)    # 4   — remove NAs first
is.na(v)
sum(is.na(v))            # how many missing
v[!is.na(v)]             # drop the NAs

# Other special values
1 / 0        # Inf
0 / 0        # NaN  (not a number)
NULL         # "nothing" — length 0


# ---------------------------------------------------------------------
# 6. STRINGS
# ---------------------------------------------------------------------
name <- "PSTAT 10"
paste("Welcome to", name)          # joins with a space
paste0("file", 1:3, ".csv")        # joins with no space, vectorized
nchar("hello")                     # number of characters
toupper("abc"); tolower("ABC")
substr("statistics", 1, 4)         # "stat"
print("quoted", quote = FALSE)
cat("cat prints without quotes or [1]\n")


# ---------------------------------------------------------------------
# 7. LISTS  — can hold different types / lengths together
# ---------------------------------------------------------------------
a_list <- list(num = c(8, 9), log = TRUE, cha = c("a", "b", "c"))
a_list
length(a_list)            # 3 items
names(a_list)

# [ ] vs [[ ]] vs $   <- classic exam question
a_list["num"]             # returns a LIST containing num
class(a_list["num"])      # "list"
a_list[["num"]]           # returns the VECTOR itself
a_list$num                # same as [["num"]]
a_list[[1]]               # by position
a_list$num[2]             # 2nd element of the num vector -> 9

a_list$num[2] <- 10       # update
a_list$new <- "added"     # add a new item
a_list$new <- NULL        # remove it

# Vectorized functions don't work on whole lists:
# mean(list(1, 2, 3))     -> error / NA
lst <- list(s1 = c(80, 90), s2 = c(70, 60))
mean(lst$s1)              # works on one element
sapply(lst, mean)         # apply mean to EACH element -> named vector
lapply(lst, mean)         # same, but returns a list


# ---------------------------------------------------------------------
# 8. MATRICES  — 2D, all same type
# ---------------------------------------------------------------------
m <- matrix(1:6, nrow = 2)     # fills by COLUMN by default
m
dim(m)
m[2, 3]           # row 2, col 3
m[1, ]            # whole row 1
m[, 2]            # whole column 2
t(m)              # transpose
m * 2             # element-wise
rowSums(m); colMeans(m)


# ---------------------------------------------------------------------
# 9. DATA FRAMES  — tables: columns can be different types
#    (this is what you'll use 90% of the time)
# ---------------------------------------------------------------------
df <- data.frame(
  name  = c("Alice", "Bob", "Carol", "Dan"),
  major = c("DS", "Stats", "CS", "DS"),
  gpa   = c(3.8, 3.2, 3.9, 2.9),
  units = c(16L, 12L, 18L, 14L)
)
df
str(df)            # structure: column names + types  (use this a lot)
nrow(df); ncol(df); dim(df)
names(df)
head(df, 2)        # first 2 rows
summary(df)        # quick stats for each column

# Accessing:  df[row, column]
df$gpa             # one column as a vector
df[["gpa"]]        # same
df[2, ]            # row 2
df[, "name"]       # column by name
df[1, 3]           # row 1, col 3
df[df$gpa > 3.5, ]                    # rows where gpa > 3.5  (note the comma!)
df[df$major == "DS", c("name", "gpa")]
subset(df, gpa > 3 & major != "CS", select = c(name, gpa))

# Modifying
df$honors <- df$gpa >= 3.5            # new column
df$gpa[df$name == "Dan"] <- 3.0       # update one value
df[order(df$gpa, decreasing = TRUE), ]  # sort rows by gpa
df <- rbind(df, data.frame(name = "Eve", major = "Stats", gpa = 3.6,
                           units = 15L, honors = TRUE))   # add a row
df

# Summaries by group
table(df$major)                               # counts per major
tapply(df$gpa, df$major, mean)                # mean gpa per major
aggregate(gpa ~ major, data = df, FUN = mean) # same, as a data frame


# ---------------------------------------------------------------------
# 10. BUILT-IN DATASETS  (great for practice)
# ---------------------------------------------------------------------
head(mtcars)                 # car data
str(mtcars)
mean(mtcars$mpg)
mtcars[mtcars$mpg > 25, c("mpg", "hp")]
table(mtcars$cyl)
tapply(mtcars$mpg, mtcars$cyl, mean)

head(iris)
summary(iris$Sepal.Length)
table(iris$Species)

# Removing rows with NA
aq <- airquality
sum(is.na(aq$Ozone))
aq_clean <- na.omit(aq)
nrow(aq); nrow(aq_clean)


# ---------------------------------------------------------------------
# 11. IMPORT / EXPORT CSV
# ---------------------------------------------------------------------
getwd()                          # where R reads/writes files by default
path <- file.path(tempdir(), "students.csv")   # temp file so we don't clutter
write.csv(df, path, row.names = FALSE)         # row.names=FALSE avoids an extra column
df2 <- read.csv(path)
str(df2)
# In real labs:  read.csv("data/whatever.csv")   (path relative to getwd())


# ---------------------------------------------------------------------
# 12. CONDITIONALS
# ---------------------------------------------------------------------
x <- -5
if (x > 0) {
  print("positive")
} else if (x == 0) {
  print("zero")
} else {
  print("negative")
}

# One-liners don't need braces
if (x < 0) -x else x

# if() only takes ONE TRUE/FALSE.  For a whole vector use ifelse():
v <- c(-2, 0, 3, 8)
ifelse(v > 0, "pos", "not pos")
ifelse(v %% 2 == 0, "even", "odd")


# ---------------------------------------------------------------------
# 13. LOOPS
# ---------------------------------------------------------------------
# for: when you know how many times
for (i in 1:5) {
  print(i^2)
}

# loop over the VALUES of a vector
nums <- c(6, 5, 3, 9, 8, 11, 6)
count_even <- 0
for (n in nums) {
  if (n %% 2 == 0) count_even <- count_even + 1
}
count_even
sum(nums %% 2 == 0)   # same answer, vectorized (preferred in R)

# filling a vector in a loop: create it first, then fill
logs <- numeric(5)            # vector of five 0s
for (i in seq_along(logs)) {  # seq_along is safer than 1:length()
  logs[i] <- log(i)
}
logs

# while: when you stop based on a condition
i <- 1
while (i < 4) {
  print(i)
  i <- i + 1                  # forget this line = infinite loop!
}

# repeat + break
x <- 1
repeat {
  if (x > 3) break
  print(x)
  x <- x + 1
}

# next = skip to the next iteration
for (i in 1:6) {
  if (i %% 2 == 1) next
  print(i)                    # prints only evens
}


# ---------------------------------------------------------------------
# 14. FUNCTIONS
# ---------------------------------------------------------------------
f_to_c <- function(temp_F) {
  temp_C <- (temp_F - 32) * 5 / 9
  return(temp_C)
}
f_to_c(82)
f_to_c(c(32, 212))     # works on vectors because the math is vectorized

# default arguments
greet <- function(name, greeting = "Hi") {
  paste(greeting, name)
}
greet("Leo")
greet("Leo", greeting = "Yo")

# returning multiple things -> return a list
describe <- function(v) {
  list(mean = mean(v), sd = sd(v), n = length(v))
}
res <- describe(mtcars$mpg)
res$mean

# last line is returned automatically (return() is optional)
square <- function(a) a^2
square(1:5)

# variables inside a function stay inside (scope)
k <- 100
change_k <- function() { k <- 5; k }
change_k()   # 5
k            # still 100


# ---------------------------------------------------------------------
# 15. APPLY FAMILY  (loop shortcuts)
# ---------------------------------------------------------------------
sapply(1:5, function(i) i^2)          # returns a vector
sapply(mtcars[, 1:3], mean)           # mean of each column
apply(m, 1, sum)                      # 1 = rows
apply(m, 2, sum)                      # 2 = columns


# ---------------------------------------------------------------------
# 16. RANDOMNESS + QUICK STATS  (useful for PSTAT 120A too)
# ---------------------------------------------------------------------
set.seed(10)                  # makes random results reproducible
sample(1:6, 10, replace = TRUE)       # roll a die 10 times
runif(3, min = 50, max = 100)         # uniform random numbers
rnorm(3, mean = 0, sd = 1)            # normal random numbers
mean(sample(1:6, 10000, replace = TRUE))   # should be close to 3.5
quantile(mtcars$mpg)
cor(mtcars$mpg, mtcars$wt)            # correlation


# ---------------------------------------------------------------------
# 17. BASE PLOTS  (show up in the plot pane / knitted file)
# ---------------------------------------------------------------------
# hist(mtcars$mpg, main = "MPG", xlab = "miles per gallon")
# plot(mtcars$wt, mtcars$mpg, xlab = "weight", ylab = "mpg")
# boxplot(mpg ~ cyl, data = mtcars)
# barplot(table(mtcars$cyl))


# ---------------------------------------------------------------------
# 18. SNEAK PEEK: tidyverse / dplyr  (L05 uses this)
#     install once:  install.packages("tidyverse")
# ---------------------------------------------------------------------
if (requireNamespace("dplyr", quietly = TRUE)) {
  library(dplyr)
  mtcars |>
    filter(mpg > 20) |>              # like SQL WHERE
    select(mpg, cyl, hp) |>          # like SQL SELECT
    arrange(desc(mpg)) |>            # like SQL ORDER BY
    head() |>
    print()

  mtcars |>
    group_by(cyl) |>                 # like SQL GROUP BY
    summarise(n = n(), avg_mpg = mean(mpg)) |>
    print()
}


# =====================================================================
#  PRACTICE  — try these yourself first!
# =====================================================================
# P1. Make a vector 2, 4, 6, ..., 20 three different ways.
# P2. From  v <- c(3, -1, 8, NA, 5, -6)  get: the positive values (no NA),
#     how many are negative, and the mean ignoring NA.
# P3. Write a function is_even(n) that returns TRUE/FALSE. Test it on 1:6.
# P4. Using a for loop, compute the sum of squares of 1:10. Then do it
#     without a loop.
# P5. Using mtcars: average hp of cars with 8 cylinders.
# P6. Using mtcars: names of cars with mpg above 30.
#     (hint: car names are rownames(mtcars))
# P7. Make a list with a name (string), scores (vector of 3 numbers),
#     and passed (logical). Extract the 2nd score.
# P8. Use ifelse to label each mtcars car "efficient" if mpg >= 25,
#     else "thirsty"; then count each label with table().


# =====================================================================
#  ANSWERS
# =====================================================================
# P1
c(2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
seq(2, 20, by = 2)
(1:10) * 2

# P2
v <- c(3, -1, 8, NA, 5, -6)
v[!is.na(v) & v > 0]
sum(v < 0, na.rm = TRUE)
mean(v, na.rm = TRUE)

# P3
is_even <- function(n) n %% 2 == 0
is_even(1:6)

# P4
total <- 0
for (i in 1:10) total <- total + i^2
total
sum((1:10)^2)

# P5
mean(mtcars$hp[mtcars$cyl == 8])

# P6
rownames(mtcars)[mtcars$mpg > 30]

# P7
me <- list(name = "Leo", scores = c(88, 92, 79), passed = TRUE)
me$scores[2]

# P8
label <- ifelse(mtcars$mpg >= 25, "efficient", "thirsty")
table(label)
