-- 创建数据库
CREATE DATABASE IF NOT EXISTS test_constraint_demo;
-- 使用数据库
USE test_constraint_demo;
-- 删除旧表
DROP TABLE IF EXISTS student;
-- 建表
CREATE TABLE student(
    id INT,
    name VARCHAR(20),
    age INT,
    gender CHAR(2)
);
-- 添加检查约束
ALTER TABLE student ADD CONSTRAINT age_check CHECK(age >= 18);
-- 查询约束名
SELECT CONSTRAINT_NAME
FROM information_schema.table_constraints
WHERE table_schema='test_constraint_demo'
AND table_name='student'
AND constraint_type='CHECK';
-- 删除约束
ALTER TABLE student DROP CONSTRAINT age_check;