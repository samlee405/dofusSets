/* tslint:disable */
/* eslint-disable */
// @generated
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL query operation: userProfile
// ====================================================

export interface userProfile_userByName {
  __typename: "User";
  id: any;
  profilePicture: string;
  creationDate: any | null;
}

export interface userProfile {
  userByName: userProfile_userByName | null;
}

export interface userProfileVariables {
  username: string;
}
