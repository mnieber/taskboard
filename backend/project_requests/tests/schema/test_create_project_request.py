query = """mutation {
  createProjectRequest(input: {
      location: "Syria",
      description: "descr",
      changemakerName: "ahmed",
      dateOfBirth: "1973-05-18",
      projectName: "C4R",
      contactAddress: "hier",
      googleDocUrl: "www.hier.com",
      descriptionUrl: "www.daar.com"
  }) {
    success,
    projectRequest {
      location
    }
  }
}"""


def test_create_project_request():
    pass
