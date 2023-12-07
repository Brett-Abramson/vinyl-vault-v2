import { ChangeEvent } from "react";
import NextLink from "next/link";
import MuiLink from "@mui/material/Link";
import Grid from "@mui/material/Grid";
import TextField from "@mui/material/TextField";
import Box from "@mui/material/Box";

interface Props {
  label: string;
  name: string;
  type: string;
  handleChange: (event: ChangeEvent<HTMLInputElement>) => void;
  value: string;
  children: string;
  link?: {
    linkText: string;
    linkUrl: string;
  };
  required?: boolean;
}

const Input = ({
  label,
  name,
  type,
  handleChange,
  value,
  children,
  link,
  required = false,
}: Props) => {
  return (
    <Grid item xs={12} sm={6}>
      {link && (
        <Box
          sx={{
            display: "flex",
            justifyContent: "flex-end",
          }}
        >
          <MuiLink component={NextLink} href={link.linkUrl} underline="hover">
            {link.linkText}
          </MuiLink>
        </Box>
      )}
      <TextField
        id={name}
        name={name}
        fullWidth
        label={label}
        type={type}
        onChange={handleChange}
        value={value}
        required={required}
      />
    </Grid>
  );
};

export default Input;

{
  /* <Input>First Name</Input> */
}
