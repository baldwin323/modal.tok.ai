# Starter React App

This is a starter React application built with TypeScript. It implements user authentication using Firebase Authentication.

## Project Structure

```
.
├── public
│   ├── index.html
│   ├── favicon.ico
│   └── manifest.json
├── src
│   ├── index.tsx
│   ├── App.tsx
│   ├── components
│   │   ├── Login.tsx
│   │   ├── SignUp.tsx
│   │   ├── Logout.tsx
│   │   ├── PrivateRoute.tsx
│   │   └── Home.tsx
│   ├── services
│   │   ├── firebase.ts
│   │   └── auth.ts
│   ├── types
│   │   └── index.ts
│   └── styles
│       ├── global.css
│       ├── Login.css
│       ├── SignUp.css
│       └── Home.css
├── .env
├── .gitignore
├── package.json
├── tsconfig.json
└── README.md
```

## Setup

1. Clone the repository
2. Install dependencies with `npm install`
3. Set up Firebase in the `.env` file
4. Run the app with `npm start`

## Features

- User Authentication: Users can sign up, log in, and log out.
- Private Routes: Some routes are protected and require authentication to access.

## Dependencies

- React
- TypeScript
- Firebase Authentication

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)