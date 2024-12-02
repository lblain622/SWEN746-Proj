-- INSERT DATA TO USERS
INSERT INTO users (username, password, email) VALUES
('john_doe', 'password123', 'john.doe@example.com'),
('jane_smith', 'password456', 'jane.smith@example.com'),
('michael_johnson', 'password789', 'michael.johnson@example.com');

-- INSERT DATA TO PROFILES
INSERT INTO profiles (first_name, last_name, age, sex, student_id, user_id) VALUES
('John', 'Doe', 30, 'M', 'S12345', 1),
('Jane', 'Smith', 25, 'F', 'S67890', 2),
('Michael', 'Johnson', 35, 'M', 'S11223', 3);

-- INSERT DATA TO SERVICES
INSERT INTO services (title, content, price, user_id) VALUES
('Web Development', 'Custom web development service', 500.00, 1),
('Graphic Design', 'Logo and branding services', 300.00, 2),
('SEO Optimization', 'Search engine optimization service', 200.00, 3);

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


-- INSERT DATA TO NOTIFICATIONS
INSERT INTO notifications (title, content, user_id) VALUES
('Project Bid Accepted', 'Your bid for the project has been accepted.', 1),
('New Message', 'You have received a new message from Jane Smith.', 1),
('Project Update', 'Michael Johnson has updated the project details.', 2);

-- INSERT DATA TO REVIEWS
INSERT INTO reviews (rating,feedback, user_id, service_id) VALUES
(5, 'Excellent service!', 1, 1),
(4, 'Good work, but room for improvement.', 2, 2),
(3, 'Average experience.', 3, 3);


