# Sample Job Descriptions for Testing

## 1. Full Stack Developer (MERN Stack)

```
We are seeking an experienced Full Stack Developer to join our dynamic team. 

Required Skills:
- Strong proficiency in MongoDB, Express.js, React.js, and Node.js
- Experience with RESTful API design and implementation
- Knowledge of HTML5, CSS3, JavaScript ES6+
- Familiarity with Git version control
- Understanding of responsive web design principles
- Experience with state management (Redux or Context API)
- Knowledge of authentication and authorization mechanisms (JWT, OAuth)

Experience Level: 3-5 years

Responsibilities:
- Develop and maintain web applications using MERN stack
- Design and implement RESTful APIs
- Collaborate with UI/UX designers
- Write clean, maintainable code
- Participate in code reviews
- Debug and troubleshoot application issues

Nice to Have:
- Experience with TypeScript
- Knowledge of Docker and Kubernetes
- Familiarity with CI/CD pipelines
- Experience with cloud platforms (AWS, Azure, or GCP)
```

## 2. Data Analyst

```
We're looking for a Data Analyst to transform data into insights that drive business value.

Required Skills:
- Strong proficiency in SQL
- Experience with Python (pandas, numpy, matplotlib)
- Knowledge of statistical analysis and hypothesis testing
- Proficiency in data visualization tools (Tableau, Power BI)
- Experience with Excel/Google Sheets for data manipulation
- Understanding of ETL processes
- Strong analytical and problem-solving skills

Experience Level: 2-4 years

Responsibilities:
- Extract, clean, and analyze large datasets
- Create dashboards and reports for stakeholders
- Identify trends and patterns in data
- Collaborate with cross-functional teams
- Present findings to non-technical audiences
- Develop and maintain data pipelines

Nice to Have:
- Experience with machine learning basics
- Knowledge of R or SAS
- Familiarity with big data tools (Spark, Hadoop)
- Experience with A/B testing
```

## 3. Python Backend Developer

```
Join our backend team to build scalable and robust APIs and services.

Required Skills:
- Expert-level Python programming
- Experience with Django or FastAPI
- Strong understanding of OOP and design patterns
- Knowledge of database systems (PostgreSQL, MySQL)
- Experience with Redis or similar caching systems
- Understanding of microservices architecture
- RESTful API design and GraphQL
- Experience with unit testing and TDD

Experience Level: 4-6 years

Responsibilities:
- Design and develop backend services and APIs
- Optimize application performance and scalability
- Implement security best practices
- Write comprehensive tests
- Collaborate with frontend developers
- Mentor junior developers
- Participate in architecture decisions

Nice to Have:
- Experience with message queues (RabbitMQ, Kafka)
- Knowledge of AWS or other cloud platforms
- Familiarity with Docker and Kubernetes
- Experience with Celery for background tasks
```

## 4. Frontend Developer (React)

```
We need a talented Frontend Developer to create amazing user experiences.

Required Skills:
- Expert knowledge of React.js and its ecosystem
- Strong proficiency in JavaScript/TypeScript
- Experience with HTML5, CSS3, SASS/LESS
- Understanding of responsive design and mobile-first approach
- Knowledge of modern frontend build tools (Webpack, Vite)
- Experience with state management (Redux, Zustand, Recoil)
- Familiarity with RESTful APIs and async operations
- Cross-browser compatibility knowledge

Experience Level: 3-5 years

Responsibilities:
- Develop user interfaces using React
- Implement responsive designs
- Optimize components for performance
- Collaborate with designers and backend developers
- Write clean, reusable component code
- Conduct code reviews
- Stay updated with latest frontend technologies

Nice to Have:
- Experience with Next.js or Gatsby
- Knowledge of testing libraries (Jest, React Testing Library)
- Familiarity with design systems
- Experience with animations (Framer Motion, GSAP)
```

## 5. DevOps Engineer

```
Looking for a DevOps Engineer to streamline our development and deployment processes.

Required Skills:
- Experience with AWS, Azure, or GCP
- Strong knowledge of Docker and Kubernetes
- Proficiency in CI/CD tools (Jenkins, GitLab CI, GitHub Actions)
- Experience with Infrastructure as Code (Terraform, CloudFormation)
- Knowledge of monitoring tools (Prometheus, Grafana, ELK stack)
- Strong scripting skills (Bash, Python)
- Understanding of networking and security principles
- Experience with configuration management (Ansible, Chef)

Experience Level: 4-7 years

Responsibilities:
- Design and implement CI/CD pipelines
- Manage cloud infrastructure and deployments
- Monitor system performance and reliability
- Implement security best practices
- Automate repetitive tasks
- Troubleshoot production issues
- Collaborate with development teams

Nice to Have:
- Kubernetes certification (CKA, CKAD)
- Experience with service mesh (Istio, Linkerd)
- Knowledge of GitOps practices
- Experience with incident management
```

## Quick Test Commands

### Test API directly:

```bash
# Register recruiter
curl -X POST http://localhost:8000/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "recruiter@test.com",
    "password": "test123",
    "full_name": "Test Recruiter",
    "role": "recruiter"
  }'

# Login
curl -X POST http://localhost:8000/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=recruiter@test.com&password=test123"

# Create job (use token from login)
curl -X POST http://localhost:8000/jobs \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "title": "Full Stack Developer",
    "description": "PASTE_JD_HERE",
    "duration_minutes": 60,
    "cutoff_percentage": 60
  }'
```
