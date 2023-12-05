import { configureStore } from "@reduxjs/toolkit";
import authReducer from "./features/authSlice";


// configure the redux store
// factory function that sets up the store with reducers and enables redux devTools in development mode
// the factory function is beneficial for server-side rendering in Next.js and for isolating store instances in testing

export const makeStore = () => {
  configureStore({
    reducer: {
      // each reducer manages its own part of the global state
      // "auth" state slace is managed by the authReducer
      auth: authReducer,
    },
    devTools: process.env.NODE_ENV !== "production",
  });
};


// the following are type definitions for convenience when using the redux store 

// AppStore type represents the type of the Redux store
export type AppStore = ReturnType<typeof makeStore>;
// RootState type represents the root state type of the Redux store
export type RootState = ReturnType<AppStore["getState"]>;
// AppDispatch type represents the dispatch type for the Redux store
export type AppDispatch = AppStore["dispatch"];

