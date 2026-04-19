CREATE TABLE IF NOT EXISTS HACKER_NEWS (
    ID INTEGER PRIMARY KEY,
    TITLE TEXT,
    USER TEXT,
    SCORE INTEGER,
    NUM_COMMENTS INTEGER,
    CATEGORY TEXT
);

INSERT INTO HACKER_NEWS (ID, TITLE, USER, SCORE, NUM_COMMENTS, CATEGORY)
VALUES
    (1, 'New AI breakthrough', 'tech_guru', 450, 120, 'Technology'),
    (2, 'Best pizza in NYC', 'foodie99', 30, 5, 'Lifestyle'),
    (3, 'How to learn SQL', 'data_wiz', 800, 300, 'Education'),
    (4, 'The future of Mars', 'space_x', 1200, 500, 'Science'),
    (5, 'Cooking with Python', 'coder_chef', 150, 45, 'Technology'),
    (6, 'History of the Internet', 'web_hist', 600, 210, 'Education'),
    (7, 'Yoga for Beginners', 'zen_master', 45, 12, 'Lifestyle');

SELECT CATEGORY, SUM(SCORE) AS Total_Score, COUNT(*) AS Article_Count
FROM HACKER_NEWS
GROUP BY CATEGORY
ORDER BY Total_Score DESC;

SELECT CATEGORY, AVG(SCORE) AS Average_Score
FROM HACKER_NEWS
GROUP BY CATEGORY
HAVING Average_Score > 100
ORDER BY Average_Score DESC;

SELECT TITLE, NUM_COMMENTS
FROM HACKER_NEWS
WHERE NUM_COMMENTS > 50
ORDER BY NUM_COMMENTS DESC
LIMIT 3;