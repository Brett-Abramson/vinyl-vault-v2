import { ChangeEvent, FormEvent } from "react";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Grid from "@mui/material/Grid";
import { Input } from "@/components/forms";
import { Spinner } from "@/components/common";

interface Config {
  label: string;
  name: string;
  type: string;
  value: string;
  required?: boolean;
  fullWidth?: boolean;
}

interface Props {
  config: Config[];
  isLoading: boolean;
  btnText: string;
  handleChange: (event: ChangeEvent<HTMLInputElement>) => void;
  handleSubmit: (event: FormEvent<HTMLFormElement>) => void;
}

const Form = ({
  config,
  isLoading,
  btnText,
  handleChange,
  handleSubmit,
}: Props) => {
  return (
    <Box component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 3 }}>
      <Grid container spacing={2}>
        {config.map((input) => (
          <Input
            key={input.name}
            label={input.label}
            name={input.name}
            type={input.type}
            handleChange={handleChange}
            value={input.value}
            required={input.required}
            fullWidth={input.fullWidth}
          >
            {input.label}
          </Input>
        ))}
      </Grid>
      <Button type="submit" fullWidth variant="contained" sx={{ mt: 3, mb: 2 }}>
        {isLoading ? <Spinner /> : `${btnText}`}
      </Button>
    </Box>
  );
};

export default Form;
