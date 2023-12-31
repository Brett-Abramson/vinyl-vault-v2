import { apiSlice } from "../services/apiSlice";

interface User {
  email: string;
}

interface SocialAuthArgs {
  provider: string;
  state: string;
  code: string;
}

interface CreateUserResponse {
  success: boolean;
  user: User;
}

// injecting endpoints here to keep services/apiSlice.ts cleaner
const authApiSlice = apiSlice.injectEndpoints({
  endpoints: (builder) => ({
    retrieveUser: builder.query<User, void>({
      query: () => "/users/me/",
    }),
    socialAuthenticate: builder.mutation({
      query: ({ provider, state, code }) => ({
        url: `/o/${provider}/?state=${encodeURIComponent(
          state
        )}&code=${encodeURIComponent(code)}`,
        method: "POST",
        header: {
          Accept: "application/json",
          "Content-Type": "application/x-www-form-urlencoded",
        },
      }),
    }),
    login: builder.mutation({
      query: ({ username, password }) => ({
        url: "/v1/jwt/create/",
        method: "POST",
        body: { username, password },
      }),
    }),
    register: builder.mutation({
      query: ({
        first_name,
        last_name,
        username,
        email,
        password,
        re_password,
      }) => ({
        url: "/users/",
        method: "POST",
        body: { first_name, last_name, username, email, password, re_password },
      }),
    }),
    verify: builder.mutation({
      query: () => ({
        url: "/v1/jwt/verify/",
        method: "POST",
      }),
    }),
    logout: builder.mutation({
      query: () => ({
        url: "/v1/logout/",
        method: "POST",
      }),
    }),
    activation: builder.mutation({
      query: ({ uid, token }) => ({
        url: `/users/activation/`,
        method: "POST",
        body: { uid, token },
      }),
    }),
    resetPassword: builder.mutation({
      query: (email) => ({
        url: `/users/reset_password/`,
        method: "POST",
        body: { email },
      }),
    }),
    resetPasswordConfirm: builder.mutation({
      query: ({ uid, token, new_password, re_new_password }) => ({
        url: `/users/reset_password_confirm/`,
        method: "POST",
        body: { uid, token, new_password, re_new_password },
      }),
    }),
  }),
});

export const {
  useRetrieveUserQuery,
  useSocialAuthenticateMutation,
  useLoginMutation,
  useRegisterMutation,
  useVerifyMutation,
  useLogoutMutation,
  useActivationMutation,
  useResetPasswordMutation,
  useResetPasswordConfirmMutation,
} = authApiSlice;
