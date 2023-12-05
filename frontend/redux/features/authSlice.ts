import { createSlice } from "@reduxjs/toolkit";

interface AuthState {
  isAuthenticated: boolean;
  isLoading: boolean;
}

const initialState = {
  // determine if a user is logged in and active or not
  isAuthenticated: false,
  // default true, using for waiting to verify a user
  isLoading: true,
} as AuthState;

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
export default authSlice.reducer;
