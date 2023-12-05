import { createSlice } from "@reduxjs/toolkit";

// define the shape of the authentication-related state
interface AuthState {
  isAuthenticated: boolean;
  isLoading: boolean;
}

const initialState = {
  isAuthenticated: false, // whether the user is authenticated
  isLoading: true, // loading state during authntication
} as AuthState;

// create a slice for authentication with reducers to handle specific actions
const authSlice = createSlice({
  name: "auth",
  initialState,
  reducers: {
    setAuth: (state) => {
      state.isAuthenticated = true;
    },
    logout: (state) => {
      state.isAuthenticated = false;
    },
    finishIntialLoad: (state) => {
      state.isLoading = false;
    },
  },
});

export const { setAuth, logout, finishIntialLoad } = authSlice.actions;
// export the reducer to be comined in the store
export default authSlice.reducer;
