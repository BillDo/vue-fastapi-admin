# Frontend - End User Site

This is the public-facing frontend application for end users, separate from the admin dashboard.

## Features

- Modern Vue 3 + Vite setup
- Clean, user-friendly interface
- Authentication and user dashboard
- Connection to the same FastAPI backend

## Project Structure

```
frontend/
├── src/
│   ├── api/          # API service functions
│   ├── assets/       # Static assets
│   ├── components/   # Reusable components
│   ├── layouts/      # Layout components
│   ├── router/       # Vue Router configuration
│   ├── store/        # Pinia state management
│   ├── styles/       # Global styles
│   ├── utils/        # Utility functions
│   └── views/        # Page components
├── public/           # Public static files
├── index.html        # HTML entry point
├── package.json      # Dependencies
└── vite.config.js    # Vite configuration
```

## Getting Started

### Install Dependencies

```bash
cd frontend
npm install
# or
pnpm install
```

### Development

```bash
npm run dev
# or
pnpm dev
```

The frontend will run on `http://localhost:3001` by default.

### Build for Production

```bash
npm run build
# or
pnpm build
```

## Configuration

The frontend connects to the FastAPI backend running on `http://localhost:9999` by default. The API proxy is configured in `vite.config.js`.

## Pages

- **Home** (`/`) - Landing page with features overview
- **About** (`/about`) - About page
- **Login** (`/login`) - User authentication
- **Dashboard** (`/dashboard`) - User dashboard (requires authentication)
- **404** - Not found page

## Technologies

- Vue 3
- Vite
- Vue Router
- Pinia
- Naive UI
- UnoCSS
- Axios

