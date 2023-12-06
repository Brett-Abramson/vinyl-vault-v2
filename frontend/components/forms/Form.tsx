import { FormEvent } from "react";
import Box from "@mui/material/Box";
import { Grid } from "@mui/material";

interface Props {
  handleSubmit: (event: FormEvent<HTMLFormElement>) => void;
}

const Form = ({ handleSubmit }: Props) => {
  return (
    <Box
      component="form"
      noValidate
      onSubmit={handleSubmit}
      sx={{ mt: 3 }}
    >
      <Grid container spacing={2}></Grid>
    </Box>
  );
};

export default Form;
