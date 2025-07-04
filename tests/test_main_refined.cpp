#include <gtest/gtest.h>

// Declare the function from main.cpp
int add(int a, int b);

TEST(AdditionTest, HandlesPositiveNumbers) {
    EXPECT_EQ(add(1, 2), 3);
}

TEST(AdditionTest, HandlesNegativeNumbers) {
    EXPECT_EQ(add(-1, -1), -2);
    EXPECT_EQ(add(-3, 3), 0);
    EXPECT_EQ(add(-5, 10), 5);
}

TEST(AdditionTest, HandlesZero) {
    EXPECT_EQ(add(0, 0), 0);
    EXPECT_EQ(add(0, 5), 5);
    EXPECT_EQ(add(-5, 0), -5);
}
