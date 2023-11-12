<a name="readme-top"></a>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Using line_profiler or memory_profiler to find CPU bound or memory bound bottleneck is very effective.
Yet to run profiling, this requires to put `@profile` decorator above the functions that we want to profile its performance.
This can become cumbersome and inefficient when we have large code base with multiple functions to profile.

Idea is to
1. pass function names as arguments in command line
2. without putting decorator on top of those functions, it will run profiling


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

### Installation

1. Clone the repo
    ```bash
    git clone git@github.com:dustinbaekpersonal/web-scraper.git
    ```

2. Create virtual environment and activate
    ```bash
    python3 -m venv .venv && source .venv/bin/activate
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>