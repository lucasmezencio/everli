<?php

class Path
{
    private const SEPARATOR = '/';
    private array $structure;

    public function __construct(string $path = self::SEPARATOR)
    {
        $this->buildStructure($path);
    }

    public function cd(string $newPath = self::SEPARATOR): void
    {
        // I Am Groot
        // oops, am I root?
        if ($newPath === self::SEPARATOR) {
            $this->structure = [self::SEPARATOR];

            return;
        }

        // If the new path starts with "/", we should consider as absolut instead of relative
        // so we reset the structure
        if (str_starts_with($newPath, self::SEPARATOR)) {
            $this->structure = [];

            $this->buildStructure($newPath);

            return;
        }

        $this->buildStructure($newPath);
    }

    private function buildStructure(string $path): void
    {
        $structure = explode(self::SEPARATOR, $path);

        foreach ($structure as $directory) {
            // Should we go to parent?
            if ($directory === '..') {
                array_pop($this->structure);

                continue;
            }

            $this->structure[] = $directory;
        }
    }

    public function __get(string $name)
    {
        if ($name === 'currentPath') {
            return implode(self::SEPARATOR, $this->structure);
        }

        return $this->{$name};
    }
}

$path = new Path('/a/b/c/d');
$path->cd('../x');
echo $path->currentPath;
