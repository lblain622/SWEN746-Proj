-- INSERT DATA TO USERS
INSERT INTO users (name, password, email) VALUES
('John Doe', 'password123', 'john.doe@example.com'),
('Jane Smith', 'password456', 'jane.smith@example.com'),
('Michael Johnson', 'password789', 'michael.johnson@example.com');

-- INSERT DATA TO PROFILES
INSERT INTO profiles (first_name, last_name, age, sex, student_id, user_id) VALUES
('John', 'Doe', 30, 'M', 'S12345', 1),
('Jane', 'Smith', 25, 'F', 'S67890', 2),
('Michael', 'Johnson', 35, 'M', 'S11223', 3);

-- INSERT Data to Category of SERVICES
INSERT INTO category_services(title) VALUES
('Tutoring'),
('Cooking'),
('Grocery Shopping'),
('Resume Writing'),
('Job Prep & Assistance'),
('Video Editing'),
('Note Taking/Summarizing'),
('Homework Help'),
('Exam Prep'),
('Pet Sitting'),
('Tech Support'),
('Fitness Training'),
('Web & App Development'),
('Art & Design'),
('Photography');



-- INSERT DATA TO SERVICES
INSERT INTO services (title,cat_id, content, price, user_id) VALUES
('Web Development',13,'Custom web development service', 500.00, 1),
('Graphic Design', 14,'Logo and branding services', 300.00, 2),
('SEO Optimization',13, 'Search engine optimization service', 200.00, 3);

-- INSERT DATA TO MESSAGES
INSERT INTO messages (title, content, to_id, from_id) VALUES
('Hello', 'Hi John, how are you?', 1, 2),
('Project Update', 'The website development is going well, I will update you soon.', 1, 3),
('Meeting Reminder', 'Just a reminder for our meeting tomorrow.', 3, 1);

-- INSERT DATA TO PAYMENTHISTORY
INSERT INTO paymentHistory (provider_name, payment_date, amount, user_id, service_id) VALUES
('John Doe', '2024-11-01', 500.00, 1, 1),
('Jane Smith', '2024-11-05', 300.00, 2, 2),
('Michael Johnson', '2024-11-10', 200.00, 3, 3);