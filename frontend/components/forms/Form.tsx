import { ChangeEvent, FormEvent } from "react";
import { Input } from "@/components/forms";
import { Spinner } from "@/components/common";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Grid from "@mui/material/Grid";

interface Config {
  label: string;
  name: string;
  type: string;
  value: string;
  link?: {
    linkText: string;
    linkUrl: string;
  };
  required?: boolean;
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
      <Grid container columns={1} spacing={2}>
        {config.map((input) => (
          <Input
            key={input.name}
            label={input.label}
            name={input.name}
            type={input.type}
            handleChange={handleChange}
            value={input.value}
            link={input.link}
            required={input.required}
          >
            {input.label}
          </Input>
        ))}
      </Grid>
      <Button type="submit" fullWidth variant="contained" disabled={isLoading} sx={{ mt: 3, mb: 2 }}>
        {isLoading ? <Spinner /> : `${btnText}`}
      </Button>
    </Box>
  );
};

export default Form;
