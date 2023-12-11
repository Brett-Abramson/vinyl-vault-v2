import { CustomLink } from "..";

interface Props {
  isSelected?: boolean;
  isMobile?: boolean;
  isBanner?: boolean;
  href: string;
  children: React.ReactNode;
  [rest: string]: any;
}

const NavLink = ({
  isSelected,
  isMobile,
  isBanner,
  href,
  children,
  ...rest
}: Props) => {
  return <CustomLink href={href}>{children}</CustomLink>;
};

export default NavLink;


// {
//   isSelected,
//   !isSelected && !isBanner,
//   isMobile,
//   !isMobile,
//   isBanner
// }