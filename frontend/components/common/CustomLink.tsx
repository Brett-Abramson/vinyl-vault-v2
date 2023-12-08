import NextLink from "next/link";
import MuiLink from "@mui/material/Link";

interface Props {
  href: string;
  linkText: string;
}

const CustomLink = ({ href, linkText }: Props) => {
  return (
    <MuiLink component={NextLink} href={href}>
      {linkText}
    </MuiLink>
  );
};

export default CustomLink;
