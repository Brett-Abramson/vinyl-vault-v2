import { apiSlice } from "../services/apiSlice";

// injecting endpoints here to keep services/apiSlice.ts cleaner
const authApiSlice = apiSlice.injectEndpoints({
  endpoints: (builder) => ({
    retrieveUser: builder.query({
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
  }),
});

export const { useRetrieveUserQuery, useSocialAuthenticateMutation } =
  authApiSlice;

// set up for google before changing to a more universal setUp
// googleAuthenticate: builder.mutation({
//   query: ({ state, code }) => ({
//     url: `/o/google-oauth2/?state=${encodeURIComponent(
//       state
//     )}&code=${encodeURIComponent(code)}`,
//     method: "POST",
//     header: {
//       Accept: "application/json",
//       "Content-Type": "application/x-www-form-urlencoded",
//     },
//   }),
// }),
