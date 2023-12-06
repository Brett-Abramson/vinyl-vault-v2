import { useRegister } from "@/hooks";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import Link from "@mui/material/Link";
import { Spinner } from "@/components/common";

const RegisterForm = () => {
  const {
    first_name,
    last_name,
    username,
    email,
    password,
    re_password,
    isLoading,
    handleChange,
    handleSubmit,
  } = useRegister();

  return (
    <Box component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 3 }}>
      <Grid container spacing={2}>
        <Grid item xs={12} sm={6}>
          <TextField
            autoComplete="given-name"
            name="first_name"
            fullWidth
            id="first_name"
            label="First Name"
            onChange={handleChange}
            value={first_name}
            autoFocus
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <TextField
            fullWidth
            id="last_name"
            label="Last Name"
            name="last_name"
            autoComplete="family-name"
            onChange={handleChange}
            value={last_name}
          />
        </Grid>
        <Grid item xs={12}>
          <TextField
            required
            fullWidth
            id="username"
            label="Username"
            name="username"
            onChange={handleChange}
            value={username}
          />
        </Grid>
        <Grid item xs={12}>
          <TextField
            required
            fullWidth
            id="email"
            label="Email Address"
            name="email"
            autoComplete="email"
            onChange={handleChange}
            value={email}
          />
        </Grid>
        <Grid item xs={12}>
          <TextField
            required
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            onChange={handleChange}
            value={password}
            // autoComplete="new-password"
          />
        </Grid>
        <Grid item xs={12}>
          <TextField
            required
            fullWidth
            name="re_password"
            label="Confirm Password"
            type="password"
            id="re_password"
            onChange={handleChange}
            value={re_password}
          />
        </Grid>
        {/* <Grid item xs={12}>
              <FormControlLabel
                control={<Checkbox value="allowExtraEmails" color="primary" />}
                label="I want to receive inspiration, marketing promotions and updates via email."
              />
            </Grid> */}
      </Grid>

      <Button type="submit" fullWidth variant="contained" sx={{ mt: 3, mb: 2 }}>
        {isLoading ? <Spinner /> : "Sign Up"}
      </Button>
    </Box>
  );
};
export default RegisterForm;
