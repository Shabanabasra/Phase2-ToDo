<!-- SYNC IMPACT REPORT
Version change: 1.0.0 → 1.1.0
Modified principles:
- Principle 1: Project Focus → Full-Stack Web Application Development
- Principle 2: Code Quality → Production-Grade Code Standards
- Principle 3: Security-First Approach (new)
- Principle 4: Authentication & Authorization (new)
- Principle 5: Data Persistence & Integrity (new)
- Principle 6: Responsive & Accessible UI (new)
Added sections: Security Requirements, Development Workflow
Removed sections: None
Templates requiring updates:
- .specify/templates/plan-template.md ✅ updated
- .specify/templates/spec-template.md ✅ updated
- .specify/templates/tasks-template.md ✅ updated
Follow-up TODOs: None
-->

# Todo Full-Stack Web Application Constitution

## Core Principles

### Full-Stack Web Application Development
All features must be implemented as a complete, integrated solution spanning both frontend and backend. The application must be developed as a modern, responsive, multi-user web application with persistent storage and authentication. Frontend (Next.js 16+ with TypeScript) and backend (FastAPI with SQLModel) must work in harmony to deliver a cohesive user experience.

### Production-Grade Code Standards
All code must meet production-grade standards: clean, readable, maintainable, and well-documented. No mock logic or placeholder implementations are allowed. Code must follow established patterns and conventions of the respective technologies (Next.js, FastAPI, SQLModel). All implementations must be complete and functional, not just proof-of-concept.

### Security-First Approach (NON-NEGOTIABLE)
Security must be the primary concern in all design and implementation decisions. All API routes require valid JWT authentication. User ID from JWT must match URL user_id. Users can only access their own tasks. Environment variables containing secrets must be properly secured. No hardcoded secrets or authentication bypasses are allowed.

### Authentication & Authorization
User authentication and authorization must be implemented using industry-standard practices. Better Auth (JWT enabled) must be used for frontend authentication. All API endpoints must validate JWT tokens with proper verification. User isolation must be enforced at the database and API levels. Authorization must follow the principle that users can only access their own data.

### Data Persistence & Integrity
All data must be persisted in PostgreSQL (Neon Serverless) using SQLModel for ORM operations. Database schema must be properly designed with appropriate relationships and constraints. Data integrity must be maintained through proper validation, error handling, and transaction management. All database operations must be efficient and secure against injection attacks.

### Responsive & Accessible UI
The user interface must be responsive and accessible across different devices and screen sizes. Frontend implementation must use modern CSS frameworks (Tailwind CSS) and follow accessibility best practices. The UI must provide a seamless experience for both desktop and mobile users. All components must be designed with user experience as a primary concern.

## Security Requirements

All API routes require valid JWT authentication. User ID from JWT must match URL user_id. Users can only access their own tasks. Environment variables must be properly managed: DATABASE_URL, BETTER_AUTH_SECRET, NEXT_PUBLIC_API_URL, and JWT_ALGORITHM must be securely configured. The single .env file must remain at project root with backend loading it explicitly using python-dotenv and frontend reading only NEXT_PUBLIC_* variables.

## Development Workflow

The monorepo structure must be maintained with frontend/ for Next.js application and backend/ for FastAPI application. All development must follow the Spec-Driven Engineering approach using Spec-Kit Plus. Each feature must have proper specifications, plans, and testable tasks. Code reviews must verify compliance with all constitution principles. All changes must be tested and validated before merging.

## Governance

The constitution supersedes all other development practices and must be followed without exception. All pull requests and code reviews must verify compliance with these principles. Any complexity must be justified with clear reasoning. The constitution can only be amended through proper documentation, approval, and migration planning.

**Version**: 1.1.0 | **Ratified**: 2025-06-13 | **Last Amended**: 2025-12-30