# Starter React App

This is a starter React application built with TypeScript. It implements user authentication using Firebase Authentication.

## Project Structure

```
.
├── public
│   ├── index.html
│   ├── favicon.ico
│   ├── manifest.json
├── src
│   ├── index.tsx
│   ├── App.tsx
│   ├── components
│   │   ├── Login.tsx
│   │   ├── SignUp.tsx
│   │   ├── Logout.tsx
│   │   ├── ProtectedRoute.tsx
│   ├── services
│   │   ├── auth.ts
│   ├── types
│   │   ├── user.ts
│   ├── styles
│   │   ├── global.css
│   │   ├── login.css
│   │   ├── signup.css
│   │   ├── logout.css
│   ├── utils
│   │   ├── firebase.ts
├── package.json
├── tsconfig.json
├── README.md
└── .gitignore
```

## Installation

1. Clone the repository
2. Install the dependencies with `npm install`
3. Start the development server with `npm start`

## Usage

- `Login.tsx`: This component provides a login form for users.
- `SignUp.tsx`: This component provides a sign up form for new users.
- `Logout.tsx`: This component allows users to log out.
- `ProtectedRoute.tsx`: This component protects routes that require authentication.
- `auth.ts`: This service provides authentication functions.
- `user.ts`: This type defines the user data structure.
- `firebase.ts`: This utility provides the Firebase configuration.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)