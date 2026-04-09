
"""
********************************************************
    Author: CBOMBS
    Date:   March 9th, 2026



*********************************************************
"""

SELECT 
    STUDENT_ID,
    SUBJECT,
    COUNT(*) AS NUMBER_OF_TIMES
FROM EXAMINATION
GROUP BY STUDENT_ID, SUBJECT;
